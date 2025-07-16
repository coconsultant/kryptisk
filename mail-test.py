import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_test_email():
    # AWS SES SMTP Configuration
    # Update these values with your specific information
    SMTP_HOST = "email-smtp.us-west-2.amazonaws.com"  # Change to your region
    SMTP_PORT = 587  # Port for STARTTLS

    # Replace with your AWS SES SMTP credentials
    SMTP_USERNAME = "AKIAS7KEZ4FWQG5NI5EV"  # Replace with your actual username
    SMTP_PASSWORD = "BAj4D+SMXIuEXzMIZI+BfUZxFRYGOnMCl60XHUjXDiZv"  # Replace with your actual password

    # Email details
    SENDER = "noreply@kryptisk.net"  # Replace with your verified sender email
    RECIPIENT = "mike@theelectricrambler.com"

    # Email content
    SUBJECT = "Test Email from AWS SES"
    BODY_TEXT = """
    Hello Mike,

    This is a test email sent using AWS SES SMTP with Python.

    Best regards,
    Your Python Script
    """

    BODY_HTML = """
    <html>
    <head></head>
    <body>
        <h2>Test Email from AWS SES</h2>
        <p>Hello Mike,</p>
        <p>This is a test email sent using <strong>AWS SES SMTP</strong> with Python.</p>
        <p>Best regards,<br>Your Python Script</p>
    </body>
    </html>
    """

    # Create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = SENDER
    msg['To'] = RECIPIENT

    # Create the plain-text and HTML version of your message
    part1 = MIMEText(BODY_TEXT, 'plain')
    part2 = MIMEText(BODY_HTML, 'html')

    # Add HTML/plain-text parts to MIMEMultipart message
    msg.attach(part1)
    msg.attach(part2)

    # Send the email
    try:
        print("Connecting to AWS SES SMTP server...")
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.ehlo()
        server.starttls()  # Enable TLS encryption
        server.ehlo()  # Re-identify ourselves after starting TLS
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        print("Sending email...")
        server.sendmail(SENDER, RECIPIENT, msg.as_string())
        server.close()

        print(f"Email sent successfully to {RECIPIENT}!")

    except Exception as e:
        print(f"Error occurred: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure your SMTP credentials are correct")
        print("2. Ensure the sender email is verified in AWS SES")
        print("3. Check if your AWS account is still in sandbox mode")
        print("4. Verify the SMTP endpoint matches your AWS region")
        print("5. Check network connectivity and firewall settings")

if __name__ == "__main__":
    send_test_email()
