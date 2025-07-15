document.addEventListener('DOMContentLoaded', function() {
    const notificationBell = document.getElementById('notification-bell');
    if (!notificationBell) {
        return;
    }

    const notificationCountBadge = document.getElementById('notification-count-badge');
    const notificationCount = document.getElementById('notification-count');
    const notificationList = document.getElementById('notification-list');
    const acknowledgeAllLink = document.getElementById('acknowledge-all-link');

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    function fetchNotificationCount() {
        fetch('/notifications/count/')
            .then(response => response.json())
            .then(data => {
                if (data.count > 0) {
                    notificationCount.textContent = data.count;
                    notificationCountBadge.style.display = 'inline-block';
                } else {
                    notificationCountBadge.style.display = 'none';
                }
            })
            .catch(error => console.error('Error fetching notification count:', error));
    }

    function fetchNotifications() {
        fetch('/notifications/list/')
            .then(response => response.json())
            .then(data => {
                notificationList.innerHTML = '';
                if (data.notifications.length > 0) {
                    acknowledgeAllLink.style.display = 'inline';
                    data.notifications.forEach(notification => {
                        const li = document.createElement('li');
                        li.className = 'list-group-item d-flex justify-content-between align-items-center';
                        li.dataset.id = notification.id;
                        li.innerHTML = `
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" value="" id="notification-check-${notification.id}">
                                <label class="form-check-label" for="notification-check-${notification.id}">
                                    ${notification.message}
                                </label>
                            </div>
                            <small class="text-muted ms-2 text-nowrap">${notification.created_at}</small>
                        `;
                        notificationList.appendChild(li);
                    });
                } else {
                    notificationList.innerHTML = '<li class="list-group-item">No unread notifications.</li>';
                    acknowledgeAllLink.style.display = 'none';
                }
            })
            .catch(error => {
                console.error('Error fetching notifications:', error);
                notificationList.innerHTML = '<li class="list-group-item">Could not load notifications.</li>';
                acknowledgeAllLink.style.display = 'none';
            });
    }

    notificationBell.addEventListener('click', function() {
        fetchNotifications();
    });

    if (notificationList) {
        notificationList.addEventListener('change', function(event) {
            if (event.target.matches('input[type="checkbox"]')) {
                const checkbox = event.target;
                const li = checkbox.closest('li');
                const notificationId = li.dataset.id;

                if (checkbox.checked) {
                    fetch(`/notifications/mark-as-read/${notificationId}/`, {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken': csrftoken,
                            'Content-Type': 'application/json'
                        }
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.status === 'success') {
                            li.classList.add('fade-out');
                            setTimeout(() => {
                                li.remove();
                                fetchNotificationCount();
                                if (notificationList.children.length === 0) {
                                    notificationList.innerHTML = '<li class="list-group-item">No unread notifications.</li>';
                                    acknowledgeAllLink.style.display = 'none';
                                }
                            }, 500); // Match CSS transition duration
                        }
                    })
                    .catch(error => console.error('Error marking notification as read:', error));
                }
            }
        });
    }

    if (acknowledgeAllLink) {
        acknowledgeAllLink.addEventListener('click', function(event) {
            event.preventDefault();
            fetch('/notifications/mark-all-as-read/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    const items = notificationList.querySelectorAll('li[data-id]');
                    items.forEach(li => {
                        li.classList.add('fade-out');
                    });
                    setTimeout(() => {
                        notificationList.innerHTML = '<li class="list-group-item">No unread notifications.</li>';
                        acknowledgeAllLink.style.display = 'none';
                        fetchNotificationCount();
                    }, 500);
                }
            })
            .catch(error => console.error('Error marking all notifications as read:', error));
        });
    }

    // Fetch count on page load and then periodically
    fetchNotificationCount();
    setInterval(fetchNotificationCount, 30000); // every 30 seconds
});
