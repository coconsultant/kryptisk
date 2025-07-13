const options = {
    debug: 'info',
    modules: {
        toolbar: '#toolbar-container'
    },
    theme: 'snow'
};
const editor = new Quill('#editor-container',options);

document.querySelector('#edit-btn').addEventListener('click', (e) => {
    document.querySelector('#bio').classList.add('d-none')
    document.querySelector('.quill-container').classList.remove('d-none')
})

document.querySelector('#edit-bio').addEventListener('click' , (e) => {
    const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value
    const data = []
    document.querySelector('.ql-editor').childNodes.forEach((node) => {
        data.push(node.outerHTML)
    })
    fetch('/profile/', {
        method: "POST",
        body:  JSON.stringify({'bio': data.join(''),'action': 'edit_bio',}),
        headers: {
            'X-CSRFToken' : csrfToken,
            'Content-Type': 'application/json'
        }
    })
        .then((response) => response.text())
        .then((res) => {console.log()})
        .catch((err) => {console.log(err)})
} )

// contact-us form
document.querySelector('#contact-form').addEventListener('submit' , (e) => {
        e.preventDefault()
        const message = document.querySelector('#message')
        const button = document.querySelector('#submit-btn')
        button.innerHTML = 'sending...'
        button.disabled = true

        fetch (`/profile/`, {
            method: "POST",
            body: new FormData(e.target),
         })
            .then((response) => {
                button.disabled = false
                button.textContent = 'Send Message'
                if(!response.ok) {
                    return response.text().then(text => { throw new Error(text) })
                } else {
                    return response.json()
                }
            })
            .then((result) => {
                message.classList.remove('text-danger')
                message.classList.add('text-success')
                message.textContent = result.message
            })
            .catch((err) => {
                message.textContent = JSON.parse( err.toString().replace('Error: ','')).message
                message.classList.add('text-danger')
                message.classList.remove('text-success')
            })
    })


document.getElementById('delete-account').onsubmit = (e) => {
    const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value
    e.preventDefault()

    fetch (`/delete_account/`, {
        method: "DELETE",
        headers: {'X-CSRFToken' : csrfToken}
    })
        .then((response) => {
            if (response.redirected)
                    window.location.href = response.url

            if (!response.ok)
                return response.text().then(text => { throw new Error(text) })
        })
        .catch((err) => {
            const error = JSON.parse(err.toString().replace('Error: ','')).errors
            document.getElementById('alert').textContent = error
        })
}