from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class UtilsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.utils'

    def ready(self):
        # Import signals to register them
        from . import signals

@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    # Only run for the authentication app and when DEBUG is true
    if sender.name == 'apps.authentication' and settings.DEBUG:
        from django.contrib.auth import get_user_model
        User = get_user_model()

        username = "mike@theelectricrambler"
        email = "mike@theelectricrambler"
        password = "asdf;lkj"
        first_name = "Mike"
        last_name = "Fischer"

        if not User.objects.filter(username=username).exists():
            print(f"Creating superuser '{username}' for development...")
            try:
                User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                print(f"Superuser '{username}' created successfully.")
            except Exception as e:
                print(f"Error creating superuser '{username}': {e}")
        else:
            print(f"Superuser '{username}' already exists. Skipping creation.")
