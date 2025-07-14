from django.apps import AppConfig
from django.conf import settings
import os

class UtilsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.utils'

    def ready(self):
        # This code will run once server starts.
        # Make sure it only runs when DEBUG is true and in the main process
        # to prevent issues with auto-reloader or management commands.
        if settings.DEBUG and os.environ.get('RUN_MAIN') == 'true':
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

