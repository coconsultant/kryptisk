TITLE: Secure Django Admin Login with Django Allauth
DESCRIPTION: This Python snippet demonstrates how to apply Django allauth's `secure_admin_login` decorator to the Django admin site's login view. This ensures that allauth's security features, such as rate limiting and two-factor authentication, are enforced for admin logins, addressing the default bypass issue.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/common/admin.rst#_snippet_0

LANGUAGE: python
CODE:
```
from django.contrib import admin
from allauth.account.decorators import secure_admin_login

admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)
```

----------------------------------------

TITLE: Configure Social Account Providers in Django Settings
DESCRIPTION: This Python code snippet demonstrates how to configure social account providers like GitHub and Google using the SOCIALACCOUNT_PROVIDERS setting in Django. It shows how to set VERIFIED_EMAIL for a provider, and how to include client credentials (client_id, secret) and fine-tune settings like scope and auth_params for specific apps or globally per provider. This method is an alternative to using SocialApp instances in the Django admin.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/socialaccount/provider_configuration.rst#_snippet_0

LANGUAGE: Python
CODE:
```
SOCIALACCOUNT_PROVIDERS = {
    "github": {
        # For each provider, you can choose whether or not the
        # email address(es) retrieved from the provider are to be
        # interpreted as verified.
        "VERIFIED_EMAIL": True
    },
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        "APPS": [
            {
                "client_id": "123",
                "secret": "456",
                "key": "",
                "settings": {
                    # You can fine tune these settings per app:
                    "scope": [
                        "profile",
                        "email"
                    ],
                    "auth_params": {
                        "access_type": "online"
                    }
                }
            }
        ],
        # The following provider-specific settings will be used for all apps:
        "SCOPE": [
            "profile",
            "email"
        ],
        "AUTH_PARAMS": {
            "access_type": "online"
        }
    }
}
```

----------------------------------------

TITLE: Add Google Provider to Django INSTALLED_APPS
DESCRIPTION: To enable Google authentication in your Django project using django-allauth, add 'allauth.socialaccount.providers.google' to your INSTALLED_APPS setting. This registers the Google social account provider with your Django application.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/socialaccount/providers/google.rst#_snippet_0

LANGUAGE: python
CODE:
```
INSTALLED_APPS = [
    ...
    'allauth.socialaccount.providers.google',
]
```

----------------------------------------

TITLE: Extending Django Allauth Base Template
DESCRIPTION: This template snippet shows the basic structure for extending 'allauth/layouts/base.html'. The '{% extends %}' tag specifies the parent template, and the '{% block content %}{% endblock %}' defines a block named 'content' where child templates can insert their specific content. This is a fundamental pattern for building consistent layouts in Django applications.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/allauth/templates/allauth/layouts/entrance.html#_snippet_0

LANGUAGE: Django Template
CODE:
```
{% extends "allauth/layouts/base.html" %} {% block content %}{% endblock %}
```

----------------------------------------

TITLE: Install Django Allauth with All Extras
DESCRIPTION: Specifies the installation of the `django-allauth` package, including all optional extras for social accounts, MFA, OIDC, OpenID, Steam, and SAML support. This line is typically used in a `pip install` command or a `requirements.txt` file.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/requirements-dev.txt#_snippet_0

LANGUAGE: Python
CODE:
```
-e ".[socialaccount,mfa,idp-oidc,openid,steam,saml]"
```

----------------------------------------

TITLE: Configure Django INSTALLED_APPS for allauth
DESCRIPTION: This snippet shows how to add the necessary `allauth` applications to your Django project's `INSTALLED_APPS` setting. It includes required modules like `allauth`, `allauth.account`, `allauth.headless`, and optional modules such as `allauth.socialaccount`, `allauth.mfa`, and `allauth.usersessions`.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/headless/installation.rst#_snippet_0

LANGUAGE: Python
CODE:
```
INSTALLED_APPS = [
    ...

    # Required
    'allauth',
    'allauth.account',
    'allauth.headless',

    # Optional
    'allauth.socialaccount',
    'allauth.mfa',
    'allauth.usersessions',

    ...
]
```

----------------------------------------

TITLE: Configure Django AUTHENTICATION_BACKENDS for django-allauth
DESCRIPTION: Adds 'allauth.account.auth_backends.AuthenticationBackend' to your Django project's AUTHENTICATION_BACKENDS setting. This enables allauth's specific authentication methods, such as login by email, alongside Django's default model backend.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/installation/quickstart.rst#_snippet_3

LANGUAGE: Python
CODE:
```
AUTHENTICATION_BACKENDS = [
    ...
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
    ...
]
```

----------------------------------------

TITLE: Add Allauth Account Middleware to Django Settings
DESCRIPTION: This snippet demonstrates how to include `allauth.account.middleware.AccountMiddleware` in Django's `MIDDLEWARE` setting. This middleware is essential for `django-allauth` to function correctly, handling user authentication and session management.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/installation/quickstart.rst#_snippet_6

LANGUAGE: Python
CODE:
```
MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",

    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
)
```

----------------------------------------

TITLE: Configure Django Allauth Social Account Providers
DESCRIPTION: This snippet shows a list of available social account providers that can be enabled in Django Allauth's `INSTALLED_APPS` setting. Each string represents a specific social media or identity provider that `django-allauth` supports for authentication.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/installation/quickstart.rst#_snippet_5

LANGUAGE: Python
CODE:
```
'allauth.socialaccount.providers.nextcloud',
'allauth.socialaccount.providers.notion',
'allauth.socialaccount.providers.odnoklassniki',
'allauth.socialaccount.providers.openid',
'allauth.socialaccount.providers.openid_connect',
'allauth.socialaccount.providers.openstreetmap',
'allauth.socialaccount.providers.orcid',
'allauth.socialaccount.providers.patreon',
'allauth.socialaccount.providers.paypal',
'allauth.socialaccount.providers.persona',
'allauth.socialaccount.providers.pinterest',
'allauth.socialaccount.providers.pocket',
"allauth.socialaccount.providers.questrade",
'allauth.socialaccount.providers.quickbooks',
'allauth.socialaccount.providers.reddit',
'allauth.socialaccount.providers.robinhood',
'allauth.socialaccount.providers.salesforce',
'allauth.socialaccount.providers.sharefile',
'allauth.socialaccount.providers.shopify',
'allauth.socialaccount.providers.slack',
'allauth.socialaccount.providers.snapchat',
'allauth.socialaccount.providers.soundcloud',
'allauth.socialaccount.providers.spotify',
'allauth.socialaccount.providers.stackexchange',
'allauth.socialaccount.providers.steam',
'allauth.socialaccount.providers.stocktwits',
'allauth.socialaccount.providers.strava',
'allauth.socialaccount.providers.stripe',
'allauth.socialaccount.providers.telegram',
'allauth.socialaccount.providers.trainingpeaks',
'allauth.socialaccount.providers.trello',
'allauth.socialaccount.providers.tumblr',
'allauth.socialaccount.providers.tumblr_oauth2',
'allauth.socialaccount.providers.twentythreeandme',
'allauth.socialaccount.providers.twitch',
'allauth.socialaccount.providers.twitter',
'allauth.socialaccount.providers.twitter_oauth2',
'allauth.socialaccount.providers.untappd',
'allauth.socialaccount.providers.vimeo',
'allauth.socialaccount.providers.vimeo_oauth2',
'allauth.socialaccount.providers.vk',
'allauth.socialaccount.providers.wahoo',
'allauth.socialaccount.providers.weibo',
'allauth.socialaccount.providers.weixin',
'allauth.socialaccount.providers.windowslive',
'allauth.socialaccount.providers.xing',
'allauth.socialaccount.providers.yahoo',
'allauth.socialaccount.providers.yandex',
'allauth.socialaccount.providers.ynab',
'allauth.socialaccount.providers.zoho',
'allauth.socialaccount.providers.zoom',
'allauth.socialaccount.providers.okta',
'allauth.socialaccount.providers.feishu',
"allauth.socialaccount.providers.atlassian",
...
```

----------------------------------------

TITLE: Extending Base Template in Django Allauth
DESCRIPTION: This snippet demonstrates a minimal Django template that extends the 'allauth/layouts/base.html' template and defines an empty 'content' block. It serves as a starting point for custom allauth pages, allowing developers to inject their specific content into the predefined layout.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/allauth/templates/allauth/layouts/manage.html#_snippet_0

LANGUAGE: Django Template
CODE:
```
{% extends "allauth/layouts/base.html" %} {% block content %}{% endblock %}
```

----------------------------------------

TITLE: Configure Django Allauth for Custom User Model with Email Login
DESCRIPTION: This snippet demonstrates how to configure `django-allauth` settings to use a custom user model where email is the primary identifier and usernames are disabled. It shows how to set the username field to `None` and adjust signup and login methods accordingly.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/account/advanced.rst#_snippet_0

LANGUAGE: Django Settings
CODE:
```
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']
ACCOUNT_LOGIN_METHODS = {'email'}
```

----------------------------------------

TITLE: Include Django Allauth URLs in Project `urls.py`
DESCRIPTION: This snippet shows how to include `django-allauth`'s URL patterns in your project's `urls.py` file. By mapping `accounts/` to `allauth.urls`, you enable all the authentication-related views provided by `allauth`, replacing or complementing Django's default authentication URLs.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/installation/quickstart.rst#_snippet_8

LANGUAGE: Python
CODE:
```
urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
    ...
]
```

----------------------------------------

TITLE: Install Django Allauth MFA Extras
DESCRIPTION: Installs the `mfa` extras for the `django-allauth` package, which are required to enable Multi-Factor Authentication features.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/mfa/introduction.rst#_snippet_0

LANGUAGE: bash
CODE:
```
pip install "django-allauth[mfa]"
```

----------------------------------------

TITLE: Integrate Google One Tap Sign-In into Django Templates
DESCRIPTION: Add this HTML snippet to your Django template to enable Google One Tap Sign-In. It includes the Google Identity Services client script and a div element configured with your client ID and the login URI for token-based authentication.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/socialaccount/providers/google.rst#_snippet_3

LANGUAGE: html
CODE:
```
<script src="//accounts.google.com/gsi/client" async></script>
<div id="g_id_onload"
         data-client_id="123-secret.apps.googleusercontent.com"
         data-login_uri="{% url 'google_login_by_token' %}">
</div>
```

----------------------------------------

TITLE: Integrate OIDC TokenAuthentication and TokenPermission with Django REST Framework
DESCRIPTION: Example demonstrating how to use TokenAuthentication and TokenPermission classes to secure a Django REST framework APIView, enforcing OIDC scope-based authorization.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/idp/openid-connect/integrations.rst#_snippet_4

LANGUAGE: python
CODE:
```
from rest_framework.views import APIView

from allauth.idp.oidc.contrib.rest_framework.authentication import TokenAuthentication
from allauth.idp.oidc.contrib.rest_framework.permissions import TokenPermission


class ResourceView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [TokenPermission.has_scope(["view-resource"])]

    def get(request, *args, **kwargs):
        ...
```

----------------------------------------

TITLE: Enable Social Account Email Authentication
DESCRIPTION: Controls whether a social login with a verified email matching an existing local user account (without a connected social account) should be treated as a login to that local account. This setting defaults to False due to security implications with untrustworthy providers and should only be enabled with fully trusted providers. It can be configured globally or per provider.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/socialaccount/configuration.rst#_snippet_2

LANGUAGE: APIDOC
CODE:
```
SOCIALACCOUNT_EMAIL_AUTHENTICATION (default: False)
  Consider a scenario where a social login occurs, and the social account comes
  with a verified email address (verified by the account provider), but that
  email address is already taken by a local user account. Additionally, assume
  that the local user account does not have any social account connected. Now,
  if the provider can be fully trusted, you can argue that we should treat this
  scenario as a login to the existing local user account even if the local
  account does not already have the social account connected, because --
  according to the provider -- the user logging in has ownership of the email
  address.  This is how this scenario is handled when
  SOCIALACCOUNT_EMAIL_AUTHENTICATION is set to True. As this implies
  that an untrustworthy provider can login to any local account by fabricating
  social account data, this setting defaults to False. Only set it to
  True if you are using providers that can be fully trusted. Instead of
  turning this on globally, you can also turn it on selectively per provider,
  for example::
```

LANGUAGE: Python
CODE:
```
SOCIALACCOUNT_PROVIDERS = {
        'google': {
            'EMAIL_AUTHENTICATION': True
        }
      }
```

----------------------------------------

TITLE: ACCOUNT_LOGIN_METHODS Setting
DESCRIPTION: Specifies the login method to use – whether the user logs in by entering their username, email address, or either one of both. Note that the login methods need to align with `ACCOUNT_SIGNUP_FIELDS`, as specifying a login method that you cannot sign up with typically points to a configuration error.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/account/configuration.rst#_snippet_14

LANGUAGE: APIDOC
CODE:
```
ACCOUNT_LOGIN_METHODS (default: {"username"}, options: "email" or "username")
```

----------------------------------------

TITLE: Configure Google OAuth Scopes and Authentication Parameters
DESCRIPTION: Customize the Google OAuth flow by defining specific scopes like 'profile' and 'email', and authentication parameters such as 'access_type' (e.g., 'online' or 'offline' for refresh tokens) within the SOCIALACCOUNT_PROVIDERS setting. This snippet also shows how to enable PKCE.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/socialaccount/providers/google.rst#_snippet_1

LANGUAGE: python
CODE:
```
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}
```

----------------------------------------

TITLE: Include allauth URLs in Django project
DESCRIPTION: This snippet demonstrates how to include `allauth`'s URL patterns in your project's `urls.py`. It includes the standard `allauth` URLs for third-party providers (even in headless mode) and the specific API endpoints for `allauth.headless`.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/headless/installation.rst#_snippet_2

LANGUAGE: Python
CODE:
```
urlpatterns = [
    # Even when using headless, the third-party provider endpoints are stil
    # needed for handling e.g. the OAuth handshake. The account views
    # can be disabled using `HEADLESS_ONLY = True`.
    path("accounts/", include("allauth.urls")),

    # Include the API endpoints:
    path("_allauth/", include("allauth.headless.urls")),
]
```

----------------------------------------

TITLE: Configure Django Allauth MFA App
DESCRIPTION: Adds the `allauth.mfa` app to the `INSTALLED_APPS` list in your Django project's `settings.py` file, enabling MFA functionality alongside other `allauth` apps.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/mfa/introduction.rst#_snippet_1

LANGUAGE: python
CODE:
```
INSTALLED_APPS = [
    ...
    # The required `allauth` apps...
    'allauth',
    'allauth.account',

    # The MFA app:
    'allauth.mfa',
    ...
]
```

----------------------------------------

TITLE: ACCOUNT_ADAPTER Configuration Setting
DESCRIPTION: Specifies the adapter class to use for Django Allauth, allowing developers to alter certain default behaviors related to account management.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/account/configuration.rst#_snippet_0

LANGUAGE: APIDOC
CODE:
```
ACCOUNT_ADAPTER (default: "allauth.account.adapter.DefaultAccountAdapter")
  Type: string
  Purpose: Specifies the adapter class to use, allowing you to alter certain default behaviour.
```

----------------------------------------

TITLE: Configure Django TEMPLATES to Override allauth Templates
DESCRIPTION: This Python code snippet demonstrates how to configure Django's `TEMPLATES` setting to enable overriding `django-allauth`'s built-in templates. By adding a project-specific template directory to `DIRS` before `APP_DIRS`, Django will prioritize your custom templates. This setup is crucial for customizing the look and feel of authentication pages.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/common/templates.rst#_snippet_0

LANGUAGE: Python
CODE:
```
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates"
        ],
        "APP_DIRS": true,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages"
            ]
        }
    }
]
```

----------------------------------------

TITLE: Retrieve Configured Social Providers with get_providers
DESCRIPTION: This template tag populates a specified template context variable with a list of all social authentication providers configured for the current site. This allows templates to dynamically display available login options, superseding older context processor methods.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/socialaccount/templates.rst#_snippet_4

LANGUAGE: Django Template
CODE:
```
{% get_providers as socialaccount_providers %}
```

----------------------------------------

TITLE: Integrate OIDC TokenAuth with Django Ninja API
DESCRIPTION: Example demonstrating how to use the TokenAuth security class to protect a Django Ninja API endpoint, requiring a specific OIDC scope for access.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/idp/openid-connect/integrations.rst#_snippet_1

LANGUAGE: python
CODE:
```
from allauth.idp.oidc.contrib.ninja.security import TokenAuth
from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/api/resource", auth=[TokenAuth(scope=["view-resource"])])
def resource(request):
    ...
```

----------------------------------------

TITLE: Configure CORS Middleware and Settings in Django
DESCRIPTION: This Python snippet demonstrates the essential configuration for enabling CORS in a Django project. It includes adding 'corsheaders.middleware.CorsMiddleware' to MIDDLEWARE, 'corsheaders' to INSTALLED_APPS, defining allowed origins, extending default allowed headers with custom ones, and enabling credentials.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/headless/cors.rst#_snippet_0

LANGUAGE: python
CODE:
```
MIDDLEWARE = (
    ...
    "corsheaders.middleware.CorsMiddleware",
    ...
)

INSTALLED_APPS = (
    ...
    "corsheaders",
    ...
)

CORS_ALLOWED_ORIGINS = [
    "https://app.project.org",
]

from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = (
    *default_headers,
    "x-session-token",
    "x-email-verification-key",
    "x-password-reset-key",
)
CORS_ALLOW_CREDENTIALS = True
```

----------------------------------------

TITLE: Define HEADLESS_FRONTEND_URLS for allauth
DESCRIPTION: This snippet defines the `HEADLESS_FRONTEND_URLS` dictionary, which maps `allauth`'s backend endpoints to the corresponding URLs in your single-page application (SPA). These URLs are used for actions like email confirmation, password reset, and signup.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/headless/installation.rst#_snippet_1

LANGUAGE: Python
CODE:
```
HEADLESS_FRONTEND_URLS = {
    "account_confirm_email": "https://app.project.org/account/verify-email/{key}",
    "account_reset_password_from_key": "https://app.org/account/password/reset/key/{key}",
    "account_signup": "https://app.org/account/signup"
}
```

----------------------------------------

TITLE: Configure WebAuthn Support in Django Allauth
DESCRIPTION: This configuration block enables WebAuthn support by including 'webauthn' in MFA_SUPPORTED_TYPES. It also shows how to optionally enable passkey login, allow insecure origins for local development (useful for localhost), and add 'django.contrib.humanize' to INSTALLED_APPS, which is required if using default templates.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/mfa/webauthn.rst#_snippet_0

LANGUAGE: Python
CODE:
```
# Make sure "webauthn" is included.
MFA_SUPPORTED_TYPES = ["totp", "webauthn", "recovery_codes"]

# Optional: enable support for logging in using a (WebAuthn) passkey.
MFA_PASSKEY_LOGIN_ENABLED = True

# Optional -- use for local development only: the WebAuthn uses the
#``fido2`` package, and versions up to including version 1.1.3 do not
# regard localhost as a secure origin, which is problematic during
# local development and testing.
MFA_WEBAUTHN_ALLOW_INSECURE_ORIGIN = True

# Add "humanize" contrib app if using default templates
INSTALLED_APPS = [
    ...
    "django.contrib.humanize",
]
```

----------------------------------------

TITLE: Django Template for Passkey Signup Page
DESCRIPTION: This template defines the structure and content for the passkey-based user signup page within a Django application using django-allauth. It extends a base entrance template, loads necessary tags, displays a signup form with CSRF protection, and includes links for existing users to sign in or explore other signup options.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/allauth/templates/account/signup_by_passkey.html#_snippet_0

LANGUAGE: Django Template
CODE:
```
{% extends "account/base\_entrance.html" %} {% load allauth i18n %} {% block head\_title %} {% trans "Signup" %} {% endblock head\_title %} {% block content %} {% element h1 %} {% trans "Passkey Sign Up" %} {% endelement %} {% setvar link %} [{% endsetvar %} {% setvar end\_link %}]({{ login_url }}) {% endsetvar %} {% element p %} {% blocktranslate %}Already have an account? Then please {{ link }}sign in{{ end\_link }}.{% endblocktranslate %} {% endelement %} {% url 'account\_signup\_by\_passkey' as action\_url %} {% element form form=form method="post" action=action\_url tags="entrance,signup" %} {% slot body %} {% csrf\_token %} {% element fields form=form unlabeled=True %} {% endelement %} {{ redirect\_field }} {% endslot %} {% slot actions %} {% element button tags="prominent,signup" type="submit" %} {% trans "Sign Up" %} {% endelement %} {% endslot %} {% endelement %} {% element hr %} {% endelement %} {% element button href=signup\_url tags="prominent,signup,outline,primary" %} {% trans "Other options" %} {% endelement %} {% endblock content %}
```

----------------------------------------

TITLE: Implement Custom Login Redirect to User Profile Page
DESCRIPTION: This Python example demonstrates how to override the `get_login_redirect_url` method in a custom `allauth` adapter to redirect users to a dynamic URL, such as their specific user profile page, after successful login.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/account/advanced.rst#_snippet_4

LANGUAGE: Python
CODE:
```
# project/settings.py:
ACCOUNT_ADAPTER = 'project.users.adapter.MyAccountAdapter'

# project/users/adapter.py:
from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = "/accounts/{username}/"
        return path.format(username=request.user.username)
```

----------------------------------------

TITLE: Configure OpenID Connect Sub-Providers in Django Allauth
DESCRIPTION: This Python configuration snippet demonstrates how to set up multiple independent OpenID Connect provider instances within Django Allauth's SOCIALACCOUNT_PROVIDERS setting. Each entry in the 'APPS' list defines a sub-provider with its unique ID, name, client credentials, and server URL. It also shows how to enable PKCE and specify token endpoint authentication methods, and notes the structure of the callback URL.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/socialaccount/providers/openid_connect.rst#_snippet_0

LANGUAGE: python
CODE:
```
SOCIALACCOUNT_PROVIDERS = {
    "openid_connect": {
        # Optional PKCE defaults to False, but may be required by your provider
        # Can be set globally, or per app (settings).
        "OAUTH_PKCE_ENABLED": True,
        "APPS": [
            {
                "provider_id": "my-server",
                "name": "My Login Server",
                "client_id": "your.service.id",
                "secret": "your.service.secret",
                "settings": {
                    "server_url": "https://my.server.example.com",
                    # Optional token endpoint authentication method.
                    # May be one of "client_secret_basic", "client_secret_post"
                    # If omitted, a method from the the server's
                    # token auth methods list is used
                    "token_auth_method": "client_secret_basic",
                    "oauth_pkce_enabled": True,
                }
            },
            {
                "provider_id": "other-server",
                "name": "Other Login Server",
                "client_id": "your.other.service.id",
                "secret": "your.other.service.secret",
                "settings": {
                    "server_url": "https://other.server.example.com"
                }
            }
        ]
    }
}
```

----------------------------------------

TITLE: Extending Base Template in Django Allauth
DESCRIPTION: This snippet illustrates the fundamental `{% extends %}` tag used in Django's template language (and Jinja2) to inherit from a parent template. It allows child templates to reuse the structure and blocks defined in a base layout, promoting consistency and reducing redundancy across web pages. The path 'allauth/layouts/manage.html' refers to a specific base template provided by the django-allauth package.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/allauth/templates/account/base_manage.html#_snippet_0

LANGUAGE: Django Template
CODE:
```
{% extends "allauth/layouts/manage.html" %}
```

----------------------------------------

TITLE: Extending a Base Template in Django
DESCRIPTION: This snippet demonstrates the basic syntax for inheriting from a parent template in Django. The `{% extends %}` tag specifies the path to the base template, allowing the current template to inherit its structure and blocks.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/allauth/templates/account/base_manage_email.html#_snippet_0

LANGUAGE: Django Template
CODE:
```
{% extends "account/base_manage.html" %}
```

----------------------------------------

TITLE: ACCOUNT_SIGNUP_FIELDS Configuration
DESCRIPTION: Specifies the list of fields to be included in the signup form. Fields marked with an asterisk are required. Options include 'username', 'email', 'phone', 'password1', 'password2', and 'email2'.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/account/configuration.rst#_snippet_6

LANGUAGE: APIDOC
CODE:
```
ACCOUNT_SIGNUP_FIELDS (default: ['username*', 'email', 'password1*', 'password2*'])
  Type: list of strings
  Purpose: Defines the fields to be completed in the signup form. Asterisked fields are required. 'email2' and 'password2' can be added for confirmation.
```

----------------------------------------

TITLE: Extending a Django Template in django-allauth
DESCRIPTION: This snippet demonstrates how a Django template extends a base layout template. It uses the `extends` tag to inherit from `allauth/layouts/entrance.html`, which is a common practice in Django projects for maintaining a consistent page structure and reducing code duplication.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/allauth/templates/mfa/base_entrance.html#_snippet_0

LANGUAGE: Django Template
CODE:
```
{% extends "allauth/layouts/entrance.html" %}
```

----------------------------------------

TITLE: Access Request Object Globally in django-allauth
DESCRIPTION: This snippet demonstrates how to access the request object globally within django-allauth. This change addresses previous inconsistencies in request availability and is essential for implementing adapter hooks and other functionalities that rely on the request context.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/release-notes/2023.rst#_snippet_0

LANGUAGE: Python
CODE:
```
from allauth.core import context
context.request
```

----------------------------------------

TITLE: Django Allauth MFA Management Template
DESCRIPTION: This template renders the user interface for managing two-factor authentication settings. It checks for supported MFA types (TOTP, WebAuthn, Recovery Codes) and displays their current status (active, inactive, number of keys/codes). It provides buttons to activate, deactivate, add, manage, view, download, or generate MFA methods based on the user's current configuration and available options.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/allauth/templates/mfa/index.html#_snippet_0

LANGUAGE: Django Template
CODE:
```
{% extends "mfa/base_manage.html" %}
{% load allauth %}
{% load i18n %}
{% block head_title %}
{% trans "Two-Factor Authentication" %}
{% endblock head_title %}
{% block content %}
{% element h1 tags="mfa,index" %}
{% trans "Two-Factor Authentication" %}
{% endelement %}
{% if "totp" in MFA_SUPPORTED_TYPES %}
{% element panel %}
{% slot title %}
{% translate "Authenticator App" %}
{% endslot %}
{% slot body %}
{% if authenticators.totp %}
{% element p %}
{% translate "Authentication using an authenticator app is active." %}
{% endelement %}
{% else %}
{% element p %}
{% translate "An authenticator app is not active." %}
{% endelement %}
{% endif %}
{% endslot %}
{% slot actions %}
{% url 'mfa_deactivate_totp' as deactivate_url %}
{% url 'mfa_activate_totp' as activate_url %}
{% if authenticators.totp %}
{% element button href=deactivate_url tags="danger,delete,panel" %}
{% translate "Deactivate" %}
{% endelement %}
{% else %}
{% element button href=activate_url tags="panel" %}
{% translate "Activate" %}
{% endelement %}
{% endif %}
{% endslot %}
{% endelement %}
{% endif %}
{% if "webauthn" in MFA_SUPPORTED_TYPES %}
{% element panel %}
{% slot title %}
{% translate "Security Keys" %}
{% endslot %}
{% slot body %}
{% if authenticators.webauthn|length %}
{% element p %}
{% blocktranslate count count=authenticators.webauthn|length %}You have added {{ count }} security key.{% plural %}You have added {{ count }} security keys.{% endblocktranslate %}
{% endelement %}
{% else %}
{% element p %}
{% translate "No security keys have been added." %}
{% endelement %}
{% endif %}
{% endslot %}
{% slot actions %}
{% if authenticators.webauthn|length %}
{% url 'mfa_list_webauthn' as webauthn_list_url %}
{% element button href=webauthn_list_url %}
{% translate "Manage" %}
{% endelement %}
{% else %}
{% url 'mfa_add_webauthn' as webauthn_add_url %}
{% element button href=webauthn_add_url %}
{% translate "Add" %}
{% endelement %}
{% endif %}
{% endslot %}
{% endelement %}
{% endif %}
{% if "recovery_codes" in MFA_SUPPORTED_TYPES %}
{% with total_count=authenticators.recovery_codes.generate_codes|length unused_count=authenticators.recovery_codes.get_unused_codes|length %}
{% element panel %}
{% slot title %}
{% translate "Recovery Codes" %}
{% endslot %}
{% slot body %}
{% if authenticators.recovery_codes %}
{% element p %}
{% blocktranslate count unused_count=unused_count %}There is {{ unused_count }} out of {{ total_count }} recovery codes available.{% plural %}There are {{ unused_count }} out of {{ total_count }} recovery codes available.{% endblocktranslate %}
{% endelement %}
{% else %}
{% element p %}
{% translate "No recovery codes set up." %}
{% endelement %}
{% endif %}
{% endslot %}
{% if is_mfa_enabled %}
{% if authenticators.recovery_codes %}
{% if unused_count > 0 %}
{% slot actions %}
{% url 'mfa_view_recovery_codes' as view_url %}
{% element button href=view_url tags="panel" %}
{% translate "View" %}
{% endelement %}
{% endslot %}
{% slot actions %}
{% url 'mfa_download_recovery_codes' as download_url %}
{% element button href=download_url tags="secondary,panel" %}
{% translate "Download" %}
{% endelement %}
{% endslot %}
{% endif %}
{% endif %}
{% slot actions %}
{% url 'mfa_generate_recovery_codes' as generate_url %}
{% element button href=generate_url tags="secondary,panel" %}
{% translate "Generate" %}
{% endelement %}
{% endslot %}
{% endif %}
{% endelement %}
{% endwith %}
{% endif %}
{% endblock content %}
```

----------------------------------------

TITLE: Migrate Database and Create Superuser for Django Allauth
DESCRIPTION: Commands to apply database migrations and create an administrative superuser for the django-allauth example application, essential for initial setup and management.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/examples/regular-django/README.org#_snippet_2

LANGUAGE: sh
CODE:
```
python manage.py migrate
python manage.py createsuperuser
```

----------------------------------------

TITLE: Configure Django Allauth Email Backend for Console Output
DESCRIPTION: This setting allows Django Allauth to print verification emails to the console instead of attempting to send them via an SMTP server. This is useful for development environments where an SMTP server might not be running, helping to avoid connectivity errors during user sign-up.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/faq.rst#_snippet_0

LANGUAGE: Python
CODE:
```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

----------------------------------------

TITLE: Django Allauth Setting: ACCOUNT_USER_MODEL_EMAIL_FIELD
DESCRIPTION: The name of the field in the custom user model that contains the email address. Refer to custom user models documentation for more details.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/account/configuration.rst#_snippet_38

LANGUAGE: APIDOC
CODE:
```
ACCOUNT_USER_MODEL_EMAIL_FIELD (default: "email")
  The name of the field containing the ``email``, if any. See custom
  user models.
```

----------------------------------------

TITLE: Integrate X-Session-Token Authentication with Django Ninja
DESCRIPTION: This snippet demonstrates how to integrate the `XSessionTokenAuth` security class with Django Ninja. It allows your Ninja API endpoints to validate authentication state using the `X-Session-Token` header provided by the client, ensuring secure access for headless applications.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/headless/integrations.rst#_snippet_0

LANGUAGE: APIDOC
CODE:
```
Class: allauth.headless.contrib.ninja.security.XSessionTokenAuth
  Type: Security Class
  Description: Authenticates requests in Django Ninja using the X-Session-Token header.
```

LANGUAGE: python
CODE:
```
from allauth.headless.contrib.ninja.security import x_session_token_auth
from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/your/own/api", auth=[x_session_token_auth])
def your_own_api(request):
    ...
```

----------------------------------------

TITLE: Account Settings: Simplified Signup Form Configuration
DESCRIPTION: Deprecated several individual signup form settings (`ACCOUNT_EMAIL_REQUIRED`, `ACCOUNT_USERNAME_REQUIRED`, `ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE`, `ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE`). These are replaced by a single new setting, `ACCOUNT_SIGNUP_FIELDS`, which offers more flexible control over required and optional signup fields (e.g., `['username*', 'email', 'password1*', 'password2*']`). This change is implemented in a backwards compatible manner.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/ChangeLog.rst#_snippet_9

LANGUAGE: APIDOC
CODE:
```
Deprecated Settings:
  - ACCOUNT_EMAIL_REQUIRED
  - ACCOUNT_USERNAME_REQUIRED
  - ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE
  - ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE

New Setting:
  - ACCOUNT_SIGNUP_FIELDS (list of strings, e.g., ['username*', 'email', 'password1*', 'password2*'])
```

----------------------------------------

TITLE: Configure Django INSTALLED_APPS for django-allauth
DESCRIPTION: Adds the required django-allauth applications ('allauth', 'allauth.account') and optionally 'allauth.socialaccount' along with specific social providers to your Django project's INSTALLED_APPS setting. This enables allauth's core functionality and social login capabilities.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/installation/quickstart.rst#_snippet_4

LANGUAGE: Python
CODE:
```
INSTALLED_APPS = [
    ...
    # The following apps are required:
    'django.contrib.auth',
    'django.contrib.messages',

    'allauth',
    'allauth.account',

    # Optional -- requires install using `django-allauth[socialaccount]`.
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.agave',
    'allauth.socialaccount.providers.amazon',
    'allauth.socialaccount.providers.amazon_cognito',
    'allauth.socialaccount.providers.angellist',
    'allauth.socialaccount.providers.apple',
    'allauth.socialaccount.providers.asana',
    'allauth.socialaccount.providers.auth0',
    'allauth.socialaccount.providers.authentiq',
    'allauth.socialaccount.providers.baidu',
    'allauth.socialaccount.providers.basecamp',
    'allauth.socialaccount.providers.battlenet',
    'allauth.socialaccount.providers.bitbucket_oauth2',
    'allauth.socialaccount.providers.bitly',
    'allauth.socialaccount.providers.box',
    'allauth.socialaccount.providers.cilogon',
    'allauth.socialaccount.providers.clever',
    'allauth.socialaccount.providers.coinbase',
    'allauth.socialaccount.providers.dataporten',
    'allauth.socialaccount.providers.daum',
    'allauth.socialaccount.providers.digitalocean',
    'allauth.socialaccount.providers.dingtalk',
    'allauth.socialaccount.providers.discord',
    'allauth.socialaccount.providers.disqus',
    'allauth.socialaccount.providers.douban',
    'allauth.socialaccount.providers.doximity',
    'allauth.socialaccount.providers.draugiem',
    'allauth.socialaccount.providers.drip',
    'allauth.socialaccount.providers.dropbox',
    'allauth.socialaccount.providers.dwolla',
    'allauth.socialaccount.providers.edmodo',
    'allauth.socialaccount.providers.edx',
    'allauth.socialaccount.providers.eventbrite',
    'allauth.socialaccount.providers.eveonline',
    'allauth.socialaccount.providers.evernote',
    'allauth.socialaccount.providers.exist',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.feedly',
    'allauth.socialaccount.providers.figma',
    'allauth.socialaccount.providers.fivehundredpx',
    'allauth.socialaccount.providers.flickr',
    'allauth.socialaccount.providers.foursquare',
    'allauth.socialaccount.providers.frontier',
    'allauth.socialaccount.providers.fxa',
    'allauth.socialaccount.providers.gitea',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.gitlab',
    'allauth.socialaccount.providers.globus',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.gumroad',
    'allauth.socialaccount.providers.hubic',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.jupyterhub',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.lemonldap',
    "allauth.socialaccount.providers.lichess",
    'allauth.socialaccount.providers.line',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.linkedin_oauth2',
    'allauth.socialaccount.providers.mailchimp',
    'allauth.socialaccount.providers.mailcow',
    'allauth.socialaccount.providers.mailru',
    'allauth.socialaccount.providers.mediawiki',
    'allauth.socialaccount.providers.meetup',
    'allauth.socialaccount.providers.miro',
    'allauth.socialaccount.providers.microsoft',
    'allauth.socialaccount.providers.naver',
```

----------------------------------------

TITLE: Displaying Non-Field Errors and Conditional Form Sections in Django Allauth Template
DESCRIPTION: This Django template snippet demonstrates how to load `allauth` template tags, iterate through and display non-field errors associated with a form, and conditionally render various sections of a form based on the `attrs.no_visible_fields` attribute. It also showcases the use of `slot` tags for defining content injection points within the template.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/examples/regular-django/example/templates/allauth/elements/form.html#_snippet_0

LANGUAGE: Django Template
CODE:
```
{% load allauth %}
{% for err in attrs.form.non_field_errors %}

{{ err }}

{% endfor %}

{% if not attrs.no_visible_fields %}

{% endif %}
{% slot body %}
{% endslot %}
{% if not attrs.no_visible_fields %}

{% endif %}
{% if not attrs.no_visible_fields %}

{% endif %}
{% slot actions %}
{% endslot %}
{% if not attrs.no_visible_fields %}

{% endif %}
```

----------------------------------------

TITLE: ACCOUNT_PREVENT_ENUMERATION Security Setting
DESCRIPTION: Controls whether information about user account existence is revealed during password reset or signup attempts. Enabling this setting prevents enumeration, but may impact immediate user feedback. It can be set to `True` for general prevention or `"strict"` for specific signup behavior.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/account/configuration.rst#_snippet_2

LANGUAGE: APIDOC
CODE:
```
ACCOUNT_PREVENT_ENUMERATION (default: True)
  Type: boolean or string ("strict")
  Purpose: Controls whether or not information is revealed about whether or not a user account exists. Set to "strict" to allow signups to go through even if email is taken, preventing enumeration at the cost of potential duplicate emails.
```

----------------------------------------

TITLE: django-allauth App API Session Token Handling
DESCRIPTION: Describes the `X-Session-Token` header mechanism for authenticating requests from non-browser applications. It outlines the lifecycle of the session token, including when to send, store, and invalidate it based on API responses.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/allauth/headless/spec/doc/description.md#_snippet_2

LANGUAGE: APIDOC
CODE:
```
X-Session-Token Header Usage:
  - Initial Request: Do not send X-Session-Token header.
  - Receiving Token: If 'meta.session_token' appears in authentication responses, store it and include in all subsequent requests as X-Session-Token header.
  - Invalid Token: If authentication response has status code 410 (Gone), remove the stored session token and restart authentication flow.
```

----------------------------------------

TITLE: Load Static Files Tag in Django Template
DESCRIPTION: This Django template tag loads the `static` template tags, enabling the use of `{% static 'path/to/file' %}` to reference static assets like CSS, JavaScript, and images. It is typically placed at the beginning of a template file where static files are needed.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/allauth/socialaccount/providers/telegram/templates/telegram/callback.html#_snippet_0

LANGUAGE: Django Template
CODE:
```
{% load static %}
```

----------------------------------------

TITLE: Django Template for Email Address Management UI
DESCRIPTION: This Django template renders the user interface for managing email addresses. It displays a list of associated email addresses, their verification and primary status, and provides forms for actions such as making an email primary, re-sending verification, removing an email, and adding a new email address.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/allauth/templates/account/email.html#_snippet_0

LANGUAGE: Django Template
CODE:
```
{% extends "account/base_manage_email.html" %}
{% load static allauth i18n %}

{% block head_title %}
  {% trans "Email Addresses" %}
{% endblock head_title %}

{% block content %}
  {% element h1 %}
    {% trans "Email Addresses" %}
  {% endelement %}

  {% if emailaddresses %}
    {% element p %}
      {% trans 'The following email addresses are associated with your account:' %}
    {% endelement %}

    {% url 'account_email' as email_url %}
    {% element form form=form action=email_url method="post" tags="email,list" %}
      {% slot body %}
        {% csrf_token %}
        {% for radio in emailaddress_radios %}
          {% with emailaddress=radio.emailaddress %}
            {% element field type="radio" checked=radio.checked name="email" value=emailaddress.email id=radio.id %}
              {% slot label %}
                {{ emailaddress.email }}
                {% if emailaddress.verified %}
                  {% element badge tags="success,email,verified" %}
                    {% translate "Verified" %}
                  {% endelement %}
                {% else %}
                  {% element badge tags="warning,email,unverified" %}
                    {% translate "Unverified" %}
                  {% endelement %}
                {% endif %}
                {% if emailaddress.primary %}
                  {% element badge tags="email,primary" %}
                    {% translate "Primary" %}
                  {% endelement %}
                {% endif %}
              {% endslot %}
            {% endelement %}
          {% endwith %}
        {% endfor %}
      {% endslot %}
      {% slot actions %}
        {% element button type="submit" name="action_primary" %}
          {% trans 'Make Primary' %}
        {% endelement %}
        {% element button tags="secondary" type="submit" name="action_send" %}
          {% trans 'Re-send Verification' %}
        {% endelement %}
        {% element button tags="danger,delete" type="submit" name="action_remove" %}
          {% trans 'Remove' %}
        {% endelement %}
      {% endslot %}
    {% endelement %}
  {% else %}
    {% include "account/snippets/warn_no_email.html" %}
  {% endif %}

  {% if can_add_email %}
    {% element h2 %}
      {% trans "Add Email Address" %}
    {% endelement %}

    {% url 'account_email' as action_url %}
    {% element form form=form method="post" action=action_url tags="email,add" %}
      {% slot body %}
        {% csrf_token %}
        {% element fields form=form %}
        {% endelement %}
      {% endslot %}
      {% slot actions %}
        {% element button name="action_add" type="submit" %}
          {% trans "Add Email" %}
        {% endelement %}
      {% endslot %}
    {% endelement %}
  {% endif %}
{% endblock content %}
```

----------------------------------------

TITLE: ACCOUNT_LOGIN_BY_CODE_ENABLED Setting
DESCRIPTION: This setting controls whether or not login by code is enabled. When set to True, users can log in using a confirmation code sent to their email.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/account/configuration.rst#_snippet_10

LANGUAGE: APIDOC
CODE:
```
ACCOUNT_LOGIN_BY_CODE_ENABLED (default: False)
```

----------------------------------------

TITLE: Create and Activate Python Virtual Environment
DESCRIPTION: Steps to create a new Python virtual environment and activate it on both Windows and macOS/Linux, isolating project dependencies. This is a crucial step for managing Python packages and ensuring a clean development setup.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/CONTRIBUTING.rst#_snippet_3

LANGUAGE: bash
CODE:
```
python -m venv virtualenv

# Activate it
# On Windows:
virtualenv\Scripts\activate
# On macOS/Linux:
source virtualenv/bin/activate
```

----------------------------------------

TITLE: Integrate Headless Session Tokens with Django Frameworks
DESCRIPTION: Out-of-the-box support has been added for using headless session tokens with popular Django frameworks like Django Ninja and Django REST framework.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/ChangeLog.rst#_snippet_17

LANGUAGE: APIDOC
CODE:
```
Integration Support:
  Frameworks:
    - Django Ninja
    - Django REST framework
  Feature: Headless session tokens
  Purpose: Enables seamless authentication token usage within these frameworks.
```

----------------------------------------

TITLE: Configure Django Allauth Apple Social Account Provider
DESCRIPTION: This Python configuration snippet for `settings.py` defines the `SOCIALACCOUNT_PROVIDERS` dictionary to enable Apple as a social account provider in Django Allauth. It requires `client_id` (your Service Identifier), `secret` (the Key ID from Apple Developer portal), `key` (your Member ID/App ID Prefix), and `certificate_key` (the content of the private key downloaded when generating the key). The `certificate_key` must be the full content of the .p8 file, including BEGIN and END PRIVATE KEY markers. For supporting both Bundle IDs (iOS mobile) and Service IDs (web), multiple app entries can be added, with the `"settings": { "hidden": True }` option used for Bundle ID apps to prevent them from appearing on web flows.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/socialaccount/providers/apple.rst#_snippet_0

LANGUAGE: python
CODE:
```
SOCIALACCOUNT_PROVIDERS = {
    "apple": {
        "APPS": [{
            # Your service identifier.
            "client_id": "your.service.id",

            # The Key ID (visible in the "View Key Details" page).
            "secret": "KEYID",

             # Member ID/App ID Prefix -- you can find it below your name
             # at the top right corner of the page, or it’s your App ID
             # Prefix in your App ID.
            "key": "MEMAPPIDPREFIX",

            "settings": {
                # The certificate you downloaded when generating the key.
                "certificate_key": """-----BEGIN PRIVATE KEY-----
s3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr
3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3
c3ts3cr3t
-----END PRIVATE KEY-----
"""
            }
        }]
    }
}
```

----------------------------------------

TITLE: OIDC IDP Configuration Settings Reference
DESCRIPTION: Defines various settings to customize the behavior of the OpenID Connect Identity Provider (IDP) in django-allauth, covering token lifetimes, adapter selection, and security features like rate limiting and refresh token rotation.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/idp/openid-connect/configuration.rst#_snippet_0

LANGUAGE: APIDOC
CODE:
```
IDP_OIDC_ACCESS_TOKEN_EXPIRES_IN:
  Type: int
  Default: 3600
  Description: The time (in seconds) after which access tokens expire.

IDP_OIDC_ADAPTER:
  Type: str
  Default: "allauth.idp.oidc.adapter.DefaultOIDCAdapter"
  Description: Specifies the adapter class to use, allowing you to alter certain default behavior.

IDP_OIDC_AUTHORIZATION_CODE_EXPIRES_IN:
  Type: int
  Default: 60
  Description: The time (in seconds) after which authorization codes expire.

IDP_OIDC_DEVICE_CODE_EXPIRES_IN:
  Type: int
  Default: 300
  Description: The time (in seconds) after which device codes expire.

IDP_OIDC_DEVICE_CODE_INTERVAL:
  Type: int
  Default: 5
  Description: The time (in seconds) a client should wait between polling attempts when using the device authorization flow.

IDP_OIDC_ID_TOKEN_EXPIRES_IN:
  Type: int
  Default: 300
  Description: The time (in seconds) after which ID tokens expire.

IDP_OIDC_PRIVATE_KEY:
  Type: str
  Default: ""
  Description: The private key used for creating ID tokens (and .well-known/jwks.json).

IDP_OIDC_RATE_LIMITS:
  Type: dict
  Default: {"device_user_code": "5/m/ip"}
  Description: Rate limit configuration.

IDP_OIDC_ROTATE_REFRESH_TOKEN:
  Type: bool
  Default: True
  Description: When access tokens are refreshed the old refresh token can be kept (False) or replaced (True) with a new one (rotated).
```

----------------------------------------

TITLE: Execute Django Database Migrations for Allauth
DESCRIPTION: This command is used to apply database migrations for `django-allauth` and other installed apps. It creates or updates the necessary database tables required for `allauth`'s functionality, such as user accounts and social connections, ensuring the database schema matches the application's models.
SOURCE: https://github.com/pennersr/django-allauth/blob/main/docs/installation/quickstart.rst#_snippet_9

LANGUAGE: Shell
CODE:
```
python manage.py migrate
```
