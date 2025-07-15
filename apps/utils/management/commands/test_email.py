from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings


class Command(BaseCommand):
    help = 'Test email configuration by sending a test email'

    def add_arguments(self, parser):
        parser.add_argument(
            '--to',
            type=str,
            help='Email address to send test email to',
            required=True
        )

    def handle(self, *args, **options):
        recipient_email = options['to']

        try:
            self.stdout.write('Testing email configuration...')
            self.stdout.write(f'Email Backend: {settings.EMAIL_BACKEND}')
            self.stdout.write(f'Email Host: {getattr(settings, "EMAIL_HOST", "Not configured")}')
            self.stdout.write(f'Email Port: {getattr(settings, "EMAIL_PORT", "Not configured")}')
            self.stdout.write(f'Email Use TLS: {getattr(settings, "EMAIL_USE_TLS", "Not configured")}')
            self.stdout.write(f'Default From Email: {getattr(settings, "DEFAULT_FROM_EMAIL", "Not configured")}')

            send_mail(
                subject='Kryptisk Email Test',
                message='This is a test email from Kryptisk to verify email configuration is working correctly.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient_email],
                fail_silently=False,
            )

            self.stdout.write(
                self.style.SUCCESS(f'Test email sent successfully to {recipient_email}')
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Failed to send test email: {str(e)}')
            )
