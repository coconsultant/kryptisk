from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.authentication'

    def ready(self):
        try:
            from django.contrib.sites.models import Site
            from django.conf import settings
            
            # Ensure correct Site configuration
            Site.objects.update_or_create(
                id=settings.SITE_ID,
                defaults={"domain": settings.SERVER, "name": "Kryptisk"}
            )
        except Exception:
            # Handle case where database might not be ready yet
            pass

