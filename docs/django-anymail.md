TITLE: Configuring Anymail settings dictionary in Django
DESCRIPTION: Example of the ANYMAIL settings dictionary in Django settings.py, showing how to configure API keys for an ESP (Mailgun in this example).
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/installation.rst#2025-04-21_snippet_2

LANGUAGE: python
CODE:
```
ANYMAIL = {
    "MAILGUN_API_KEY": "<your Mailgun key>",
}
```

----------------------------------------

TITLE: Sending HTML Email with Inline Images and Anymail Extensions
DESCRIPTION: Advanced email example using Anymail's extended features. This includes sending HTML content with inline images, setting metadata and tags, and enabling click tracking - demonstrating Anymail's ESP-specific features with a portable API.
SOURCE: https://github.com/anymail/django-anymail/blob/main/README.rst#2025-04-21_snippet_3

LANGUAGE: python
CODE:
```
from django.core.mail import EmailMultiAlternatives
from anymail.message import attach_inline_image_file

msg = EmailMultiAlternatives(
    subject="Please activate your account",
    body="Click to activate your account: https://example.com/activate",
    from_email="Example <admin@example.com>",
    to=["New User <user1@example.com>", "account.manager@example.com"],
    reply_to=["Helpdesk <support@example.com>"])

# Include an inline image in the html:
logo_cid = attach_inline_image_file(msg, "/path/to/logo.jpg")
html = """<img alt="Logo" src="cid:{logo_cid}">
          <p>Please <a href="https://example.com/activate">activate</a>
          your account</p>""".format(logo_cid=logo_cid)
msg.attach_alternative(html, "text/html")

# Optional Anymail extensions:
msg.metadata = {"user_id": "8675309", "experiment_variation": 1}
msg.tags = ["activation", "onboarding"]
msg.track_clicks = True

# Send it:
msg.send()
```

----------------------------------------

TITLE: Installing Django-Anymail with ESP-specific dependencies using pip
DESCRIPTION: Command to install Django-Anymail package with optional ESP-specific dependencies. The example includes SendGrid and SparkPost, but users can specify other ESPs as needed.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/installation.rst#2025-04-21_snippet_0

LANGUAGE: console
CODE:
```
$ pip install "django-anymail[sendgrid,sparkpost]"
```

----------------------------------------

TITLE: Enabling Anymail Debug API Requests in Django
DESCRIPTION: When set to True, this setting enables output of raw API communication with the ESP for debugging purposes. It dumps each HTTP request and ESP response to sys.stdout once the response is received. This should not be enabled in production due to security risks.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/installation.rst#2025-04-21_snippet_12

LANGUAGE: python
CODE:
```
ANYMAIL_DEBUG_API_REQUESTS = True
```

----------------------------------------

TITLE: Configuring Django Settings for Anymail with Mailgun
DESCRIPTION: Django settings configuration for Anymail integration. This includes adding 'anymail' to INSTALLED_APPS, configuring Mailgun-specific settings, setting the email backend, and defining default email addresses.
SOURCE: https://github.com/anymail/django-anymail/blob/main/README.rst#2025-04-21_snippet_1

LANGUAGE: python
CODE:
```
INSTALLED_APPS = [
    # ...
    "anymail",
    # ...
]

ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": "<your Mailgun key>",
    "MAILGUN_SENDER_DOMAIN": 'mg.example.com',  # your Mailgun domain, if needed
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
DEFAULT_FROM_EMAIL = "you@example.com"  # if you don't already have this in settings
SERVER_EMAIL = "your-server@example.com"  # ditto (default from-email for Django errors)
```

----------------------------------------

TITLE: Sending a Basic Email with Django and Anymail
DESCRIPTION: A simple example of sending an email using Django's send_mail function with Anymail. This demonstrates how Anymail integrates seamlessly with Django's standard email functionality.
SOURCE: https://github.com/anymail/django-anymail/blob/main/README.rst#2025-04-21_snippet_2

LANGUAGE: python
CODE:
```
from django.core.mail import send_mail

send_mail("It works!", "This will get sent through Mailgun",
          "Anymail Sender <from@example.com>", ["to@example.com"])
```

----------------------------------------

TITLE: Configuring ESP-specific Global Defaults in Django Settings (Python)
DESCRIPTION: This snippet demonstrates how to set ESP-specific global defaults in the Django settings. It shows how to override general defaults for specific ESPs like Postmark and Mailgun.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/sending/anymail_additions.rst#2025-04-21_snippet_16

LANGUAGE: python
CODE:
```
ANYMAIL = {
    ...
    "SEND_DEFAULTS": {
        "tags": ["kryptisk", "version3"],
    },
    "POSTMARK_SEND_DEFAULTS": {
        # Postmark only supports a single tag
        "tags": ["version3"],  # overrides SEND_DEFAULTS['tags'] (not merged!)
    },
    "MAILGUN_SEND_DEFAULTS": {
        "esp_extra": {"o:dkim": "no"},  # Disable Mailgun DKIM signatures
    },
}
```

----------------------------------------

TITLE: Setting up Django EMAIL_BACKEND for Anymail
DESCRIPTION: Configuration for Django's EMAIL_BACKEND setting to use Anymail's Mailgun backend for sending emails.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/installation.rst#2025-04-21_snippet_3

LANGUAGE: python
CODE:
```
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
```

----------------------------------------

TITLE: Using ESP Templates with Merge Data in Django-Anymail
DESCRIPTION: Example demonstrating how to send an email using an ESP stored template with per-recipient merge data and global merge data. This code sets up a batch send where each recipient receives a personalized message.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/sending/templates.rst#2025-04-21_snippet_0

LANGUAGE: python
CODE:
```
from django.core.mail import EmailMessage

message = EmailMessage(
    subject=None,  # use the subject in our stored template
    from_email="marketing@example.com",
    to=["Wile E. <wile@example.com>", "rr@example.com"])
message.template_id = "after_sale_followup_offer"  # use this ESP stored template
message.merge_data = {  # per-recipient data to merge into the template
    'wile@example.com': {'NAME': "Wile E.",
                         'OFFER': "15% off anvils"},
    'rr@example.com':   {'NAME': "Mr. Runner"},
}
message.merge_global_data = {  # merge data for all recipients
    'PARTNER': "Acme, Inc.",
    'OFFER': "5% off any Acme product",  # a default if OFFER missing for recipient
}
message.send()
```

----------------------------------------

TITLE: Generating random webhook secret using Django's crypto utilities
DESCRIPTION: Command to generate a secure random string for use as an Anymail webhook secret. This creates two 16-character random strings separated by a colon.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/installation.rst#2025-04-21_snippet_5

LANGUAGE: console
CODE:
```
$ python -c "from django.utils import crypto; print(':'.join(crypto.get_random_string(16) for _ in range(2)))"
```

----------------------------------------

TITLE: Implementing MailerSend Advanced Personalization with Django Anymail
DESCRIPTION: This example demonstrates how to create an on-the-fly email template using MailerSend's advanced personalization variables. It shows how to set up merge data for individual recipients and global merge data for all recipients.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/mailersend.rst#2025-04-21_snippet_6

LANGUAGE: python
CODE:
```
message = EmailMessage(
    from_email="shipping@example.com",
    subject="Your order {{ order_no }} has shipped",
    body="""Hi {{ name }},
            We shipped your order {{ order_no }}
            on {{ ship_date }}.""",
    to=["alice@example.com", "Bob <bob@example.com>"]
)
# (you'd probably also set a similar html body with variables)
message.merge_data = {
    "alice@example.com": {"name": "Alice", "order_no": "12345"},
    "bob@example.com": {"name": "Bob", "order_no": "54321"},
}
message.merge_global_data = {
    "ship_date": "May 15"  # Anymail maps globals to all recipients
}
# (see discussion of batch-send-mode below)
message.esp_extra = {
    "batch-send-mode": "use-bulk-email"
}
```

----------------------------------------

TITLE: Implementing Inbound Email Handler in Django Anymail
DESCRIPTION: Example of implementing an inbound email signal receiver that processes incoming messages. The handler prints the sender's email, envelope sender, and subject of each received message.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/inbound.rst#2025-04-21_snippet_0

LANGUAGE: python
CODE:
```
from anymail.signals import inbound
from django.dispatch import receiver

@receiver(inbound)  # add weak=False if inside some other function/class
def handle_inbound(sender, event, esp_name, **kwargs):
    message = event.message
    print("Received message from %s (envelope sender %s) with subject '%s'" % (
          message.from_email, message.envelope_sender, message.subject))
```

----------------------------------------

TITLE: Initializing AnymailMessage with ESP Features in Python
DESCRIPTION: Demonstrates creating an AnymailMessage object with additional ESP-specific attributes like tags and metadata. Shows how to access the send status after sending the message.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/sending/anymail_additions.rst#2025-04-21_snippet_0

LANGUAGE: python
CODE:
```
from anymail.message import AnymailMessage

message = AnymailMessage(
    subject="Welcome",
    body="Welcome to our site",
    to=["New User <user1@example.com>"],
    tags=["Onboarding"],  # Anymail extra in constructor
)
# Anymail extra attributes:
message.metadata = {"onboarding_experiment": "variation 1"}
message.track_clicks = True

message.send()
status = message.anymail_status  # available after sending
status.message_id  # e.g., '<12345.67890@example.com>'
status.recipients["user1@example.com"].status  # e.g., 'queued'
```

----------------------------------------

TITLE: Configuring additional Anymail settings
DESCRIPTION: Examples of various Anymail configuration options, including IGNORE_RECIPIENT_STATUS which controls exception behavior for invalid recipients.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/installation.rst#2025-04-21_snippet_7

LANGUAGE: python
CODE:
```
ANYMAIL = {
    ...
    "IGNORE_RECIPIENT_STATUS": True,
}
```

----------------------------------------

TITLE: Setting Per-Recipient Merge Metadata in Python
DESCRIPTION: Shows how to set per-recipient metadata for batch sending. Each recipient gets individualized metadata, which can be used for tracking and later retrieval.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/sending/anymail_additions.rst#2025-04-21_snippet_3

LANGUAGE: python
CODE:
```
message.to = ["wile@example.com", "Mr. Runner <rr@example.com>"]
message.merge_metadata = {
    "wile@example.com": {"customer": 123, "order": "acme-zxyw"},
    "rr@example.com": {"customer": 45678, "order": "acme-wblt"},
}
```

----------------------------------------

TITLE: Using Global Send Defaults with AnymailMessage (Python)
DESCRIPTION: This code snippet shows how to use AnymailMessage with global send defaults. It demonstrates how message-specific attributes are merged with the global defaults, and how to override or ignore specific default values.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/sending/anymail_additions.rst#2025-04-21_snippet_15

LANGUAGE: python
CODE:
```
message = AnymailMessage(...)
message.tags = ["welcome"]
message.metadata = {"source": "Ads", "user_id": 12345}
message.track_clicks = False

message.send()
# will send with:
#   tags: ["kryptisk", "version3", "welcome"] (merged with defaults)
#   metadata: {"district": "North", "source": "Ads", "user_id": 12345} (merged)
#   track_clicks: False (message overrides defaults)
#   track_opens: True (from the defaults)
```

----------------------------------------

TITLE: Testing Email Sending with Anymail Test Backend in Django
DESCRIPTION: This example demonstrates how to test email sending in Django using Anymail's test EmailBackend. It shows how to verify that emails are sent correctly, check email attributes, and inspect Anymail-specific parameters that would be sent to the ESP.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/tips/testing.rst#2025-04-21_snippet_0

LANGUAGE: python
CODE:
```
from django.core import mail
from django.test import TestCase
from django.test.utils import override_settings

@override_settings(EMAIL_BACKEND='anymail.backends.test.EmailBackend')
class SignupTestCase(TestCase):
    # Assume our app has a signup view that accepts an email address...
    def test_sends_confirmation_email(self):
        self.client.post("/account/signup/", {"email": "user@example.com"})

        # Test that one message was sent:
        self.assertEqual(len(mail.outbox), 1)

        # Verify attributes of the EmailMessage that was sent:
        self.assertEqual(mail.outbox[0].to, ["user@example.com"])
        self.assertEqual(mail.outbox[0].tags, ["confirmation"])  # an Anymail custom attr

        # Or verify the Anymail params, including any merged settings defaults:
        self.assertTrue(mail.outbox[0].anymail_test_params["track_clicks"])
```

----------------------------------------

TITLE: Implementing Email Tracking Event Handlers with Anymail
DESCRIPTION: Example of setting up Django signal receivers to handle email tracking events. Shows how to implement separate handlers for bounced emails and clicked links using the Anymail tracking signal.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/sending/tracking.rst#2025-04-21_snippet_0

LANGUAGE: python
CODE:
```
from anymail.signals import tracking
from django.dispatch import receiver

@receiver(tracking)  # add weak=False if inside some other function/class
def handle_bounce(sender, event, esp_name, **kwargs):
    if event.event_type == 'bounced':
        print("Message %s to %s bounced" % (
              event.message_id, event.recipient))

@receiver(tracking)
def handle_click(sender, event, esp_name, **kwargs):
    if event.event_type == 'clicked':
        print("Recipient %s clicked url %s" % (
              event.recipient, event.click_url))
```

----------------------------------------

TITLE: Using Brevo Templates with Merge Data in Django Anymail
DESCRIPTION: Demonstrates how to use Brevo templates with Django Anymail, including setting the template ID and providing merge data for personalization.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/brevo.rst#2025-04-21_snippet_3

LANGUAGE: python
CODE:
```
message = EmailMessage(
    # (subject and body come from the template, so don't include those)
    to=["alice@example.com", "Bob <bob@example.com>"]
)
message.template_id = 3   # use this Brevo template
message.from_email = None  # to use the template's default sender
message.merge_data = {
    'alice@example.com': {'name': "Alice", 'order_no': "12345"},
    'bob@example.com': {'name': "Bob", 'order_no': "54321"},
}
message.merge_global_data = {
    'ship_date': "May 15",
}
```

----------------------------------------

TITLE: Configuring Mailgun Email Backend in Django
DESCRIPTION: Sets up Anymail's Mailgun backend as the Django email backend handler
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/mailgun.rst#2025-04-21_snippet_0

LANGUAGE: python
CODE:
```
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
```

----------------------------------------

TITLE: Implementing Email Blocklist with Pre-send Signal in Python
DESCRIPTION: Example of using Anymail's pre_send signal to filter blocked email recipients before sending. The code checks both the from_email and recipient addresses against a blocklist, canceling sends or removing blocked recipients as needed.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/sending/signals.rst#2025-04-21_snippet_0

LANGUAGE: python
CODE:
```
from anymail.exceptions import AnymailCancelSend
from anymail.signals import pre_send
from django.dispatch import receiver
from email.utils import parseaddr

from your_app.models import EmailBlockList

@receiver(pre_send)
def filter_blocked_recipients(sender, message, **kwargs):
    # Cancel the entire send if the from_email is blocked:
    if not ok_to_send(message.from_email):
        raise AnymailCancelSend("Blocked from_email")
    # Otherwise filter the recipients before sending:
    message.to = [addr for addr in message.to if ok_to_send(addr)]
    message.cc = [addr for addr in message.cc if ok_to_send(addr)]

def ok_to_send(addr):
    # This assumes you've implemented an EmailBlockList model
    # that holds emails you want to reject...
    name, email = parseaddr(addr)  # just want the <email> part
    try:
        EmailBlockList.objects.get(email=email)
        return False  # in the blocklist, so *not* OK to send
    except EmailBlockList.DoesNotExist:
        return True  # *not* in the blocklist, so OK to send
```

----------------------------------------

TITLE: Configuring Global Send Defaults in Django Settings (Python)
DESCRIPTION: This snippet demonstrates how to set up global send defaults for Anymail in the Django settings file. It includes examples of setting metadata, tags, and tracking options that will apply to all messages sent through Anymail.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/sending/anymail_additions.rst#2025-04-21_snippet_14

LANGUAGE: python
CODE:
```
ANYMAIL = {
    ...
    "SEND_DEFAULTS": {
        "metadata": {"district": "North", "source": "unknown"},
        "tags": ["kryptisk", "version3"],
        "track_clicks": True,
        "track_opens": True,
    },
}
```

----------------------------------------

TITLE: Using MailerSend Stored Templates with Django Anymail
DESCRIPTION: This example shows how to use a pre-existing MailerSend template stored in your account. It demonstrates setting the template_id and how template defaults can override message attributes.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/mailersend.rst#2025-04-21_snippet_7

LANGUAGE: python
CODE:
```
message = EmailMessage(
    from_email="shipping@example.com",
    # (subject and body from template)
    to=["alice@example.com", "Bob <bob@example.com>"]
)
message.template_id = "vzq12345678"  # id of template in our account
# ... set merge_data and merge_global_data as above
```

----------------------------------------

TITLE: Accessing Message ID from Anymail Status Response
DESCRIPTION: Shows how to access the message_id property from the anymail_status attribute after sending a message. This example demonstrates accessing an RFC 2822 style message ID.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/sending/anymail_additions.rst#2025-04-21_snippet_8

LANGUAGE: python
CODE:
```
message.anymail_status.message_id
# '<20160306015544.116301.25145@example.org>'
```

----------------------------------------

TITLE: Sending Emails with Multiple Backends in Django-Anymail
DESCRIPTION: This code snippet demonstrates how to send emails using different email backends in a Django application with Anymail. It shows sending via the default Mailgun backend, an SMTP backend, a SendGrid backend, and a Mailgun backend with custom credentials.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/tips/multiple_backends.rst#2025-04-21_snippet_0

LANGUAGE: python
CODE:
```
from django.core.mail import send_mail, get_connection

# send_mail connection defaults to the settings EMAIL_BACKEND, which
# we've set to Anymail's Mailgun EmailBackend. This will be sent using Mailgun:
send_mail("Thanks", "We sent your order", "sales@example.com", ["customer@example.com"])

# Get a connection to an SMTP backend, and send using that instead:
smtp_backend = get_connection('django.core.mail.backends.smtp.EmailBackend')
send_mail("Uh-Oh", "Need your attention", "admin@example.com", ["alert@example.com"],
          connection=smtp_backend)

# You can even use multiple Anymail backends in the same app:
sendgrid_backend = get_connection('anymail.backends.sendgrid.EmailBackend')
send_mail("Password reset", "Here you go", "noreply@example.com", ["user@example.com"],
          connection=sendgrid_backend)

# You can override settings.py settings with kwargs to get_connection.
# This example supplies credentials for a different Mailgun sub-acccount:
alt_mailgun_backend = get_connection('anymail.backends.mailgun.EmailBackend',
                                     api_key=MAILGUN_API_KEY_FOR_MARKETING)
send_mail("Here's that info", "you wanted", "info@marketing.example.com", ["prospect@example.org"],
          connection=alt_mailgun_backend)
```

----------------------------------------

TITLE: Sending AMP Email with Django's EmailMultiAlternatives
DESCRIPTION: Demonstrates how to send an AMP email along with plain text and HTML alternatives using Django's EmailMultiAlternatives class.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/sending/django_email.rst#2025-04-21_snippet_2

LANGUAGE: python
CODE:
```
from django.core.mail import EmailMultiAlternatives

msg = EmailMultiAlternatives("Subject", "text body",
                             "from@example.com", ["to@example.com"])
msg.attach_alternative("<!doctype html><html amp4email data-css-strict>...",
                       "text/x-amp-html")
msg.attach_alternative("<!doctype html><html>...", "text/html")
msg.send()
```

----------------------------------------

TITLE: Updating Django Settings from SendinBlue to Brevo
DESCRIPTION: Diff showing how to update Django settings from SendinBlue to Brevo branding, including changing the email backend path and renaming configuration settings.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/brevo.rst#2025-04-21_snippet_8

LANGUAGE: diff
CODE:
```
- EMAIL_BACKEND = "anymail.backends.sendinblue.EmailBackend"  # old
+ EMAIL_BACKEND = "anymail.backends.brevo.EmailBackend"       # new

  ANYMAIL = {
      ...
-     "SENDINBLUE_API_KEY": "<your v3 API key>",  # old
+     "BREVO_API_KEY": "<your v3 API key>",       # new
      # (Also change "SENDINBLUE_API_URL" to "BREVO_API_URL" if present)

      # If you are using Brevo-specific global send defaults, change:
-     "SENDINBLUE_SEND_DEFAULTS" = {...},  # old
+     "BREVO_SEND_DEFAULTS" = {...},       # new
  }
```

----------------------------------------

TITLE: Configuring SendGrid Backend for Django Anymail
DESCRIPTION: Sets the EmailBackend in Django settings to use Anymail's SendGrid integration. This is the first required configuration step to start using SendGrid with Anymail.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/sendgrid.rst#2025-04-21_snippet_0

LANGUAGE: python
CODE:
```
EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
```

----------------------------------------

TITLE: Composing Email with Django Templates in Python
DESCRIPTION: This snippet demonstrates how to build an email message using Django's render_to_string function to generate the subject, text body, and HTML body from separate template files. It uses a merge_data dictionary for template context and creates a multipart email with both text and HTML versions.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/tips/django_templates.rst#2025-04-21_snippet_0

LANGUAGE: python
CODE:
```
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

merge_data = {
    'ORDERNO': "12345", 'TRACKINGNO': "1Z987"
}

subject = render_to_string("message_subject.txt", merge_data).strip()
text_body = render_to_string("message_body.txt", merge_data)
html_body = render_to_string("message_body.html", merge_data)

msg = EmailMultiAlternatives(subject=subject, from_email="store@example.com",
                             to=["customer@example.com"], body=text_body)
msg.attach_alternative(html_body, "text/html")
msg.send()
```

----------------------------------------

TITLE: Setting Mailgun API Key
DESCRIPTION: Configures the required API key for sending emails through Mailgun
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/mailgun.rst#2025-04-21_snippet_1

LANGUAGE: python
CODE:
```
ANYMAIL = {
    ...
    "MAILGUN_API_KEY": "<your API key>",
}
```

----------------------------------------

TITLE: Configuring Advanced Amazon SES Options with esp_extra
DESCRIPTION: Python example demonstrating how to use esp_extra to access advanced Amazon SES features like configuration sets and custom email tags.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/amazon_ses.rst#2025-04-21_snippet_4

LANGUAGE: python
CODE:
```
message.esp_extra = {
    # Override AMAZON_SES_CONFIGURATION_SET_NAME for this message:
    'ConfigurationSetName': 'NoOpenOrClickTrackingConfigSet',
    # Authorize a custom sender:
    'FromEmailAddressIdentityArn': 'arn:aws:ses:us-east-1:123456789012:identity/example.com',
    # Set SES Message Tags (change to 'DefaultEmailTags' for template sends):
    'EmailTags': [

```

----------------------------------------

TITLE: Configuring Amazon SES Template Message in Python
DESCRIPTION: Demonstrates how to set up a templated email message using Amazon SES with Django-Anymail. It shows setting the template ID, merge data, and global merge data.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/amazon_ses.rst#2025-04-21_snippet_5

LANGUAGE: python
CODE:
```
message = EmailMessage(
    from_email="shipping@example.com",
    # you must omit subject and body (or set to None) with Amazon SES templates
    to=["alice@example.com", "Bob <bob@example.com>"]
)
message.template_id = "MyTemplateName"  # Amazon SES TemplateName
message.merge_data = {
    'alice@example.com': {'name': "Alice", 'order_no': "12345"},
    'bob@example.com': {'name': "Bob", 'order_no': "54321"},
}
message.merge_global_data = {
    'ship_date': "May 15",
}
```

----------------------------------------

TITLE: Implementing Email Logging with Post-send Signal in Python
DESCRIPTION: Example of using Anymail's post_send signal to log sent messages. The code creates database records for each recipient with details about the message status and delivery.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/sending/signals.rst#2025-04-21_snippet_1

LANGUAGE: python
CODE:
```
from anymail.signals import post_send
from django.dispatch import receiver

from your_app.models import SentMessage

@receiver(post_send)
def log_sent_message(sender, message, status, esp_name, **kwargs):
    # This assumes you've implemented a SentMessage model for tracking sends.
    # status.recipients is a dict of email: status for each recipient
    for email, recipient_status in status.recipients.items():
        SentMessage.objects.create(
            esp=esp_name,
            message_id=recipient_status.message_id,  # might be None if send failed
            email=email,
            subject=message.subject,
            status=recipient_status.status,  # 'sent' or 'rejected' or ...
        )
```

----------------------------------------

TITLE: Configuring Mailjet API Credentials
DESCRIPTION: Configures the Mailjet API key and secret key in Django settings. These credentials are required for authentication with Mailjet's API.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/mailjet.rst#2025-04-21_snippet_1

LANGUAGE: python
CODE:
```
ANYMAIL = {
    "MAILJET_API_KEY": "<your API key>",
    "MAILJET_SECRET_KEY": "<your API secret>"
}
```

----------------------------------------

TITLE: Using Double Quotes for Display-Names in Email Addresses in Python
DESCRIPTION: Demonstrates how to properly format email addresses containing commas or parentheses in the display-name portion. Per RFC 5322, double quotes must be used around display-names that contain special characters like commas.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/sending/exceptions.rst#2025-04-21_snippet_0

LANGUAGE: python
CODE:
```
# won't work:
send_mail(from_email='Widgets, Inc. <widgets@example.com>', ...)
# must use double quotes around display-name containing comma:
send_mail(from_email='"Widgets, Inc." <widgets@example.com>', ...)
```

----------------------------------------

TITLE: Using Mailgun Stored Templates
DESCRIPTION: Example demonstrating the use of Mailgun stored templates with handlebars syntax ({{ }}). Shows template_id usage with merge data and global merge data.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/mailgun.rst#2025-04-21_snippet_8

LANGUAGE: python
CODE:
```
message = EmailMessage(
    from_email="shipping@example.com",
    # The message body and html_body come from from the stored template.
    # (You can still use %recipient.___% fields in the subject:)
    subject="Your order %recipient.order_no% has shipped",
    to=["alice@example.com", "Bob <bob@example.com>"]
)
message.template_id = 'shipping-notification'  # name of template in our account
# The substitution data is exactly the same as in the previous example:
message.merge_data = {
    'alice@example.com': {'name': "Alice", 'order_no': "12345"},
    'bob@example.com': {'name': "Bob", 'order_no': "54321"},
}
message.merge_global_data = {
    'ship_date': "May 15"  # Anymail maps globals to all recipients
}
```

----------------------------------------

TITLE: Configuring Batch Sending with SparkPost Templates in Python
DESCRIPTION: This snippet demonstrates how to set up a message for batch sending using SparkPost templates and merge data. It shows how to use template_id, set merge_data for individual recipients, and use merge_global_data for shared values across all recipients.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/sparkpost.rst#2025-04-21_snippet_4

LANGUAGE: python
CODE:
```
message = EmailMessage(
    ...
    to=["alice@example.com", "Bob <bob@example.com>"]
)
message.template_id = "11806290401558530"  # SparkPost id
message.from_email = None  # must set after constructor (see below)
message.merge_data = {
    'alice@example.com': {'name': "Alice", 'order_no': "12345"},
    'bob@example.com': {'name': "Bob", 'order_no': "54321"},
}
message.merge_global_data = {
    'ship_date': "May 15",
    # Can use SparkPost's special "dynamic" keys for nested substitutions (see notes):
    'dynamic_html': {
        'status_html': "<a href='https://example.com/order/{{order_no}}'>Status</a>",
    },
    'dynamic_plain': {
        'status_plain': "Status: https://example.com/order/{{order_no}}",
    },
}
```

----------------------------------------

TITLE: Using SendGrid-specific Features with esp_extra
DESCRIPTION: Example showing how to use SendGrid features not directly supported by Anymail by setting the esp_extra attribute. This example configures subscription management and custom tracking settings.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/sendgrid.rst#2025-04-21_snippet_3

LANGUAGE: python
CODE:
```
message.open_tracking = True
message.esp_extra = {
    "asm": {  # SendGrid subscription management
        "group_id": 1,
        "groups_to_display": [1, 2, 3],
    },
    "tracking_settings": {
        "open_tracking": {
            # Anymail will automatically set `"enable": True` here,
            # based on message.open_tracking.
            "substitution_tag": "%%OPEN_TRACKING_PIXEL%%",
        },
    },
    # Because "personalizations" is a dict, Anymail will merge "future_feature"
    # into the SendGrid personalizations array for each message recipient
    "personalizations": {
        "future_feature": {"future": "data"},
    },
}
```

----------------------------------------

TITLE: Setting Brevo-specific Parameters with esp_extra
DESCRIPTION: Demonstrates how to use the esp_extra attribute to set Brevo-specific parameters, such as batchId for scheduled sending.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/brevo.rst#2025-04-21_snippet_1

LANGUAGE: python
CODE:
```
message.esp_extra = {
    'batchId': '275d3289-d5cb-4768-9460-a990054b6c81',  # merged into send params
}
```

----------------------------------------

TITLE: Handling JPEG Attachments in Django with Anymail
DESCRIPTION: Demonstrates how to process a JPEG image attachment from an inbound email and assign it to a user's profile avatar in Django. It includes content type checking and security validation.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/inbound.rst#2025-04-21_snippet_3

LANGUAGE: python
CODE:
```
# allow users to mail in jpeg attachments to set their profile avatars...
if attachment.get_content_type() == "image/jpeg":
    # for security, you must verify the content is really a jpeg
    # (you'll need to supply the is_valid_jpeg function)
    if is_valid_jpeg(attachment.get_content_bytes()):
        user.profile.avatar_image = attachment.as_uploaded_file()
```

----------------------------------------

TITLE: Creating On-the-Fly Template with Merge Fields in Python
DESCRIPTION: This snippet illustrates how to create an on-the-fly template using merge fields directly in the EmailMessage's subject and body. It also shows how to set the merge field format for Handlebars-style fields.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/sendgrid.rst#2025-04-21_snippet_6

LANGUAGE: python
CODE:
```
# on-the-fly template using merge fields in subject and body:
message = EmailMessage(
    subject="Your order {{order_no}} has shipped",
    body="Dear {{name}}:\nWe've shipped order {{order_no}}.",
    to=["alice@example.com", "Bob <bob@example.com>"]
)
# note: no template_id specified
message.merge_data = {
    'alice@example.com': {'name': "Alice", 'order_no': "12345"},
    'bob@example.com': {'name': "Bob", 'order_no': "54321"},
}
message.esp_extra = {
    # here's how to get Handlebars-style {{merge}} fields with Python's str.format:
    'merge_field_format': "{{{{{}}}}"  # "{{ {{ {} }} }}" without the spaces
}
```

----------------------------------------

TITLE: Configuring Resend Webhook Signing Secret in Django Settings
DESCRIPTION: This snippet shows how to add the Resend webhook signing secret to the Django settings.py file. The secret is used for validating webhook signatures from Resend.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/resend.rst#2025-04-21_snippet_6

LANGUAGE: python
CODE:
```
ANYMAIL = {
    # ...
    "RESEND_SIGNING_SECRET": "whsec_..."
}
```

----------------------------------------

TITLE: Accessing Mailgun Event Data in Python
DESCRIPTION: This snippet demonstrates how to access the Mailgun event-data ID from an Anymail tracking event. It's useful for integrating with Mailgun's other event APIs.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/mailgun.rst#2025-04-21_snippet_10

LANGUAGE: python
CODE:
```
event.esp_event["event-data"]["id"]
```

----------------------------------------

TITLE: Sending Email with Unisender Go Template and Merge Data in Python
DESCRIPTION: This snippet demonstrates how to send an email using a Unisender Go template with merge data. It sets the template ID, recipient-specific merge data, and global merge data.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/unisender_go.rst#2025-04-21_snippet_5

LANGUAGE: python
CODE:
```
message = EmailMessage(
    to=["alice@example.com", "Bob <bob@example.com>"],
)
message.from_email = None  # Use template From email and name
message.template_id = "0000aaaa-1111-2222-3333-4444bbbbcccc"
message.merge_data = {
    "alice@example.com": {"name": "Alice", "order_no": "12345"},
    "bob@example.com": {"name": "Bob", "order_no": "54321"},
}
message.merge_global_data = {
    "ship_date": "15-May",
}
message.send()
```

----------------------------------------

TITLE: Sending Email with Unisender Go Inline Template in Python
DESCRIPTION: This example shows how to send an email using an inline Unisender Go template. It includes subject and body templates with merge variables, and sets up recipient-specific and global merge data.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/unisender_go.rst#2025-04-21_snippet_6

LANGUAGE: python
CODE:
```
message = EmailMessage(
    from_email="shipping@example.com",
    to=["alice@example.com", "Bob <bob@example.com>"],
    # Use {{substitution}} variables in subject and body:
    subject="Your order {{order_no}} has shipped",
    body="""Hi {{name}},
            We shipped your order {{order_no}}
            on {{ship_date}}.""",
)
# (You'd probably also want to add an HTML body here.)
# The substitution data is exactly the same as in the previous example:
message.merge_data = {
    "alice@example.com": {"name": "Alice", "order_no": "12345"},
    "bob@example.com": {"name": "Bob", "order_no": "54321"},
}
message.merge_global_data = {
    "ship_date": "May 15",
}
message.send()
```

----------------------------------------

TITLE: Setting MailerSend API Token in Django Settings
DESCRIPTION: Configures the required API token for authenticating with MailerSend's email service. This token should have full access to email features but no access to other features.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/mailersend.rst#2025-04-21_snippet_1

LANGUAGE: python
CODE:
```
ANYMAIL = {
    ...
    "MAILERSEND_API_TOKEN": "<your API token>",
}
```

----------------------------------------

TITLE: Configuring Postmark Email Backend in Django
DESCRIPTION: Sets up the Postmark email backend in Django settings.py
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/postmark.rst#2025-04-21_snippet_0

LANGUAGE: python
CODE:
```
EMAIL_BACKEND = "anymail.backends.postmark.EmailBackend"
```

----------------------------------------

TITLE: Configuring Brevo Email Backend in Django Settings
DESCRIPTION: Sets up the Brevo email backend in Django's settings.py file. This includes specifying the backend class and the API key required for authentication.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/brevo.rst#2025-04-21_snippet_0

LANGUAGE: python
CODE:
```
EMAIL_BACKEND = "anymail.backends.brevo.EmailBackend"

ANYMAIL = {
    ...
    "BREVO_API_KEY": "<your v3 API key>",
}
```

----------------------------------------

TITLE: Implementing Mailgun Recipient Variables Template
DESCRIPTION: Example showing how to use Mailgun's recipient variables (%recipient.___%) syntax for on-the-fly email templating with merge data and global merge data.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/mailgun.rst#2025-04-21_snippet_7

LANGUAGE: python
CODE:
```
message = EmailMessage(
    from_email="shipping@example.com",
    # Use %recipient.___% syntax in subject and body:
    subject="Your order %recipient.order_no% has shipped",
    body="""Hi %recipient.name%,
            We shipped your order %recipient.order_no%
            on %recipient.ship_date%.""",
    to=["alice@example.com", "Bob <bob@example.com>"]
)
# (you'd probably also set a similar html body with %recipient.___% variables)
message.merge_data = {
    'alice@example.com': {'name': "Alice", 'order_no': "12345"},
    'bob@example.com': {'name': "Bob", 'order_no': "54321"},
}
message.merge_global_data = {
    'ship_date': "May 15"  # Anymail maps globals to all recipients
}
```

----------------------------------------

TITLE: Configuring IAM Policy for Amazon SES Operations
DESCRIPTION: IAM policy JSON that grants permissions for sending emails via SES, confirming SNS subscriptions, and accessing S3 for inbound mail. Includes permissions for both templated and non-templated sends.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/amazon_ses.rst#2025-04-21_snippet_10

LANGUAGE: json
CODE:
```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "ses:SendEmail",
      "ses:SendRawEmail",
      "ses:SendBulkEmail",
      "ses:SendBulkTemplatedEmail"
    ],
    "Resource": "*"
  }, {
    "Effect": "Allow",
    "Action": ["sns:ConfirmSubscription"],
    "Resource": ["arn:aws:sns:*:*:*"]
  }, {
    "Effect": "Allow",
    "Action": ["s3:GetObject"],
    "Resource": ["arn:aws:s3:::MY-PRIVATE-BUCKET-NAME/MY-INBOUND-PREFIX/*"]
  }]
}
```

----------------------------------------

TITLE: Using On-the-fly Templates with Merge Fields
DESCRIPTION: Shows how to use merge fields directly in the email message body without creating a stored template in Mailjet.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/mailjet.rst#2025-04-21_snippet_4

LANGUAGE: python
CODE:
```
message = EmailMessage(
    from_email="orders@example.com",
    to=["alice@example.com", "Bob <bob@example.com>"],
    subject="Your order has shipped",
    body="Dear [[var:name]]: Your order [[var:order_no]] shipped on [[var:ship_date]]."
)
message.merge_data = {
    'alice@example.com': {'name': "Alice", 'order_no': "12345"},
    'bob@example.com': {'name': "Bob", 'order_no': "54321"}
}
message.merge_global_data = {
    'ship_date': "May 15"
}
```

----------------------------------------

TITLE: Configuring Mandrill Email Backend in Django Settings
DESCRIPTION: Sets the Django EMAIL_BACKEND setting to use Anymail's Mandrill backend for sending emails.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/mandrill.rst#2025-04-21_snippet_0

LANGUAGE: python
CODE:
```
EMAIL_BACKEND = "anymail.backends.mandrill.EmailBackend"
```

----------------------------------------

TITLE: Checking Message Status in Anymail
DESCRIPTION: Examples showing how to check the status of a sent message using the status attribute of anymail_status. Demonstrates different status responses and checking for successful delivery.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/sending/anymail_additions.rst#2025-04-21_snippet_10

LANGUAGE: python
CODE:
```
message1.anymail_status.status
# set(['queued'])  # all recipients were queued
message2.anymail_status.status
# set(['rejected', 'sent'])  # at least one recipient was sent,
                             # and at least one rejected

# This is an easy way to check there weren't any problems:
if message3.anymail_status.status.issubset({'queued', 'sent'}):
    print("ok!")
```

----------------------------------------

TITLE: Testing Email Tracking Webhooks in Django-Anymail
DESCRIPTION: This example shows how to test Anymail's event tracking webhooks by creating simulated AnymailTrackingEvent objects and sending them to your signal receivers. It includes verification of how your code processes delivery and bounce events.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/tips/testing.rst#2025-04-21_snippet_1

LANGUAGE: python
CODE:
```
from anymail.signals import AnymailTrackingEvent, tracking
from django.test import TestCase

class EmailTrackingTests(TestCase):
    def test_delivered_event(self):
        # Build an AnymailTrackingEvent with event_type (required)
        # and any other attributes your receiver cares about. E.g.:
        event = AnymailTrackingEvent(
            event_type="delivered",
            recipient="to@example.com",
            message_id="test-message-id",
        )

        # Invoke all registered Anymail tracking signal receivers:
        tracking.send(sender=object(), event=event, esp_name="TestESP")

        # Verify expected behavior of your receiver. What to test here
        # depends on how your code handles the tracking events. E.g., if
        # you create a Django model to store the event, you might check:
        from kryptisk.models import MyTrackingModel
        self.assertTrue(MyTrackingModel.objects.filter(
            email="to@example.com", event="delivered",
            message_id="test-message-id",
        ).exists())

    def test_bounced_event(self):
        # ... as above, but with `event_type="bounced"`
        # etc.
```

----------------------------------------

TITLE: Setting Mandrill API Key in Django Settings
DESCRIPTION: Configures the Mandrill API key in the Django settings file, which is required for authenticating with the Mandrill service.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/mandrill.rst#2025-04-21_snippet_1

LANGUAGE: python
CODE:
```
ANYMAIL = {
    ...
    "MANDRILL_API_KEY": "<your API key>",
}
```

----------------------------------------

TITLE: Enabling Open Tracking for Individual Messages in Python
DESCRIPTION: Shows how to enable open tracking for a specific email message, overriding the ESP's default settings.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/sending/anymail_additions.rst#2025-04-21_snippet_5

LANGUAGE: python
CODE:
```
message.track_opens = True
```

----------------------------------------

TITLE: Configuring Mandrill Template with Merge Data
DESCRIPTION: Shows how to use a Mandrill template with merge fields and provide per-recipient merge data for batch sending.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/mandrill.rst#2025-04-21_snippet_3

LANGUAGE: python
CODE:
```
message = EmailMessage(
    ...
    subject="Your order *|order_no|* has shipped",
    body="""Hi *|name|*,
            We shipped your order *|order_no|*
            on *|ship_date|*.""",
    to=["alice@example.com", "Bob <bob@example.com>"]
)
# (you'd probably also set a similar html body with merge fields)
message.merge_data = {
    'alice@example.com': {'name': "Alice", 'order_no': "12345"},
    'bob@example.com': {'name': "Bob", 'order_no': "54321"},
}
message.merge_global_data = {
    'ship_date': "May 15",
}
```

----------------------------------------

TITLE: Testing Inbound Email Processing in Django-Anymail
DESCRIPTION: This example demonstrates how to test inbound email processing by creating simulated AnymailInboundMessage and AnymailInboundEvent objects. It shows how to construct test messages and verify that your code correctly processes received emails.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/tips/testing.rst#2025-04-21_snippet_2

LANGUAGE: python
CODE:
```
from anymail.inbound import AnymailInboundMessage
from anymail.signals import AnymailInboundEvent, inbound
from django.test import TestCase

class EmailReceivingTests(TestCase):
    def test_inbound_event(self):
        # Build a simple AnymailInboundMessage and AnymailInboundEvent
        # (see tips for more complex messages after the example):
        message = AnymailInboundMessage.construct(
            from_email="user@example.com", to="comments@example.net",
            subject="subject", text="text body", html="html body")
        event = AnymailInboundEvent(message=message)

        # Invoke all registered Anymail inbound signal receivers:
        inbound.send(sender=object(), event=event, esp_name="TestESP")

        # Verify expected behavior of your receiver. What to test here
        # depends on how your code handles the inbound message. E.g., if
        # you create a user comment from the message, you might check:
        from kryptisk.models import MyCommentModel
        comment = MyCommentModel.objects.get(poster="user@example.com")
        self.assertEqual(comment.text, "text body")
```

----------------------------------------

TITLE: Configuring MailerSend Inbound Secret in Django Settings
DESCRIPTION: This snippet shows how to set up the MAILERSEND_INBOUND_SECRET in the Django settings.py file. This secret is used by Anymail to verify calls to the inbound endpoint.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/mailersend.rst#2025-04-21_snippet_9

LANGUAGE: python
CODE:
```
ANYMAIL = {
    # ...
    "MAILERSEND_INBOUND_SECRET": "<secret you copied>"
}
```

----------------------------------------

TITLE: Accessing Batch Send Message IDs in Python
DESCRIPTION: Example of how to access individual message IDs for batch sends using Anymail. This snippet shows how to get the message ID for a specific recipient email address from the anymail_status object.
SOURCE: https://github.com/anymail/django-anymail/blob/main/CHANGELOG.rst#2025-04-21_snippet_2

LANGUAGE: Python
CODE:
```
message.anymail_status.recipients[to_email].message_id
```

----------------------------------------

TITLE: Using Mailjet Templates with Merge Data
DESCRIPTION: Demonstrates how to use Mailjet templates with merge data for personalized emails. Includes setting template ID and providing recipient-specific merge data.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/mailjet.rst#2025-04-21_snippet_3

LANGUAGE: python
CODE:
```
message = EmailMessage(
    to=["alice@example.com", "Bob <bob@example.com>"]
)
message.template_id = "176375"
message.from_email = None
message.merge_data = {
    'alice@example.com': {'name': "Alice", 'order_no': "12345"},
    'bob@example.com': {'name': "Bob", 'order_no': "54321"}
}
message.merge_global_data = {
    'ship_date': "May 15"
}
```

----------------------------------------

TITLE: Sending Email with SendGrid Dynamic Template in Python
DESCRIPTION: This snippet demonstrates how to send an email using a SendGrid dynamic template with Django-Anymail. It shows how to set the template ID, provide merge data for personalization, and include global merge data.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/sendgrid.rst#2025-04-21_snippet_4

LANGUAGE: python
CODE:
```
message = EmailMessage(
    ...
    # omit subject and body (or set to None) to use template content
    to=["alice@example.com", "Bob <bob@example.com>"]
)
message.template_id = "d-5a963add2ec84305813ff860db277d7a"  # SendGrid dynamic id
message.merge_data = {
    'alice@example.com': {'name': "Alice", 'order_no': "12345"},
    'bob@example.com': {'name': "Bob", 'order_no': "54321"},
}
message.merge_global_data = {
    'ship_date': "May 15",
}
```

----------------------------------------

TITLE: Configuring MailerSend Inbound Email Secret for Inbound Routing
DESCRIPTION: Sets the inbound route secret needed to verify inbound email notifications from MailerSend, required only when using inbound email routing.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/mailersend.rst#2025-04-21_snippet_4

LANGUAGE: python
CODE:
```
ANYMAIL = {
    ...
    "MAILERSEND_INBOUND_SECRET": "<secret from inbound management page>",
}
```

----------------------------------------

TITLE: Implementing Batch Sending with Resend using Anymail
DESCRIPTION: This code snippet shows how to use Anymail's merge_metadata for batch sending with Resend, including per-recipient metadata.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/resend.rst#2025-04-21_snippet_5

LANGUAGE: python
CODE:
```
message = EmailMessage(
    to=["alice@example.com", "Bob <bob@example.com>"],
    from_email="...", subject="...", body="..."
)
message.merge_metadata = {
    'alice@example.com': {'user_id': "12345"},
    'bob@example.com': {'user_id': "54321"},
}
```

----------------------------------------

TITLE: Configuring SendGrid Legacy Template with Merge Field Format in Python
DESCRIPTION: This example shows how to use a SendGrid legacy template with Django-Anymail. It demonstrates setting the template ID, providing merge data, and specifying the merge field format in the esp_extra attribute.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/sendgrid.rst#2025-04-21_snippet_5

LANGUAGE: python
CODE:
```
# ...
message.template_id = "5997fcf6-2b9f-484d-acd5-7e9a99f0dc1f"  # SendGrid legacy id
message.merge_data = {
    'alice@example.com': {'name': "Alice", 'order_no': "12345"},
    'bob@example.com': {'name': "Bob", 'order_no': "54321"},
}
message.esp_extra = {
    # Tell Anymail this SendGrid legacy template uses "-field-" for merge fields.
    # (You could instead set SENDGRID_MERGE_FIELD_FORMAT in your ANYMAIL settings.)
    'merge_field_format': "-{}-"
}
```

----------------------------------------

TITLE: Using SparkPost Advanced Features with esp_extra
DESCRIPTION: Example of using esp_extra to access SparkPost-specific features not directly supported by Anymail, such as setting transactional options, IP pools, templates, and recipient lists.
SOURCE: https://github.com/anymail/django-anymail/blob/main/docs/esps/sparkpost.rst#2025-04-21_snippet_3

LANGUAGE: python
CODE:
```
message.esp_extra = {
    "options": {
        # Treat as transactional for unsubscribe and suppression:
        "transactional": True,
        # Override your default dedicated IP pool:
        "ip_pool": "transactional_pool",
    },
    # Add a description:
    "description": "Test-run for new templates",
    "content": {
        # Use draft rather than published template:
        "use_draft_template": True,
        # Use an A/B test:
        "ab_test_id": "highlight_support_links",
    },
    # Use a stored recipients list (overrides message to/cc/bcc):
    "recipients": {
        "list_id": "design_team"
    },
}
```
