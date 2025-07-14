from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
from django.conf import settings

class Command(BaseCommand):
    help = 'Sends a test email using the configured Django email settings.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--recipient',
            dest='recipient_email',
            default=None, # Will use SITE_OWNER_MAIL from settings if not explicitly provided
            help='The email address to send the test email to. Defaults to SITE_OWNER_MAIL.',
        )

    def handle(self, *args, **options):
        recipient_email = options['recipient_email']

        # Determine the recipient email, falling back to SITE_OWNER_MAIL
        if not recipient_email and hasattr(settings, 'SITE_OWNER_MAIL') and settings.SITE_OWNER_MAIL:
            recipient_email = settings.SITE_OWNER_MAIL
        
        if not recipient_email:
            raise CommandError('Recipient email not specified. Set SITE_OWNER_MAIL in .env or provide --recipient argument.')

        if not hasattr(settings, 'DEFAULT_FROM_EMAIL') or not settings.DEFAULT_FROM_EMAIL:
            raise CommandError('DEFAULT_FROM_EMAIL is not configured in settings. Cannot send email.')

        try:
            send_mail(
                'Kryptisk Test Email',
                'This is a test email sent from your Kryptisk application. If you received this, your email settings are working!',
                settings.DEFAULT_FROM_EMAIL,
                [recipient_email],
                fail_silently=False,
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully sent test email to {recipient_email}'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error sending test email to {recipient_email}: {e}'))
