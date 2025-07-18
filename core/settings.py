# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, environ, sys, random, string

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 32 ))

# Render Deployment Code
DEBUG = 'RENDER' not in os.environ

# Assets Management
ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')

# load production server from .env
ALLOWED_HOSTS        = ['localhost', 'localhost:85', '127.0.0.1', 'kryptisk.net', env('SERVER', default='127.0.0.1') ]
CSRF_TRUSTED_ORIGINS = ['http://localhost:85', 'http://127.0.0.1', 'https://kryptisk.net', 'https://' + env('SERVER', default='127.0.0.1') ]

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    CSRF_TRUSTED_ORIGINS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.home',  # Enable the inner home (home)
    'apps.authentication',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.twitter',
    "sslserver",
    'apps.utils', # Added for startup utility functions
    'apps.notifications',
    'apps.qrcode_generator',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware', # Added this line
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"  # Route defined in home/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in home/urls.py
LOGIN_URL = "/login/"
TEMPLATE_DIR = os.path.join(CORE_DIR, "apps/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.context_processors.cfg_assets_root',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DB_ENGINE   = os.getenv('DB_ENGINE'   , None)
DB_USERNAME = os.getenv('DB_USERNAME' , None)
DB_PASS     = os.getenv('DB_PASS'     , None)
DB_HOST     = os.getenv('DB_HOST'     , None)
DB_PORT     = os.getenv('DB_PORT'     , None)
DB_NAME     = os.getenv('DB_NAME'     , None)

if DB_ENGINE and DB_NAME and DB_USERNAME:
    DATABASES = {
      'default': {
        'ENGINE'  : 'django.db.backends.' + DB_ENGINE,
        'NAME'    : DB_NAME,
        'USER'    : DB_USERNAME,
        'PASSWORD': DB_PASS,
        'HOST'    : DB_HOST,
        'PORT'    : DB_PORT,
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'apps/static'),
    os.path.join(BASE_DIR, 'static'), # This line was added/modified
)

# Media files (for user uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#############################################################
#############################################################
AUTH_USER_MODEL = 'authentication.CustomUser'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SITE_OWNER_PHONE      = os.getenv('SITE_OWNER_PHONE'     , None)
SITE_OWNER_MAIL       = os.getenv('SITE_OWNER_MAIL'      , None)
SITE_OWNER_ADDRESS    = os.getenv('SITE_OWNER_ADDRESS'   , None)
SITE_OWNER_FBK        = os.getenv('SITE_OWNER_FBK'       , None)
SITE_OWNER_TWITTER    = os.getenv('SITE_OWNER_TWITTER'   , None)
SITE_OWNER_INSTAGRAM  = os.getenv('SITE_OWNER_INSTAGRAM' , None)

# Email settings for django-allauth
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('AWS_SES_REGION_ENDPOINT')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587)) # Changed default port from 587 to 465
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('AWS_SMTP_USERNAME')
EMAIL_HOST_PASSWORD = os.getenv('AWS_SMTP_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('AWS_DEFAULT_FROM_EMAIL')
EMAIL_SENDER = os.getenv('AWS_SENDER_EMAIL')
EMAIL_USE_SSL= False


# Allauth specific settings
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
#ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_FIELDS = ["email*", "username*", "password1*", "password2*"]
#ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_LOGIN_METHODS = {'email', 'username'}  # For "username_email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'home'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_EMAIL_FROM = os.getenv('EMAIL_SENDER')

GITHUB_ID     = os.getenv('GITHUB_ID'    , None) # Corrected syntax here, removed extra '
GITHUB_SECRET = os.getenv('GITHUB_SECRET', None)
GITHUB_AUTH   = GITHUB_SECRET is not None and GITHUB_ID is not None

TWITTER_ID     = os.getenv('TWITTER_ID'    , None)
TWITTER_SECRET = os.getenv('TWITTER_SECRET', None)
TWITTER_AUTH   = TWITTER_SECRET is not None and TWITTER_ID is not None


AUTHENTICATION_BACKENDS = (
    "allauth.account.auth_backends.AuthenticationBackend",
)

SERVER = env('SERVER', default='127.0.0.1')

if DEBUG:
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http' if sys.argv[1] == 'runserver' else 'https'
else:
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'  # assumed production http protocol is https

# LOGIN_REDIRECT_URL is set higher up as "home" already and should be fine.
# LOGIN_REDIRECT_URL = f'{ACCOUNT_DEFAULT_HTTP_PROTOCOL}://localhost:{8000 if DEBUG else 80}/' # This line makes it absolute, which might conflict. Removing it.

SOCIALACCOUNT_PROVIDERS = {}
if GITHUB_AUTH:
    SOCIALACCOUNT_PROVIDERS['github'] = {
        'APP': {
            'client_id': GITHUB_ID,
            'secret': GITHUB_SECRET,
            'key': ''
        }
    }
if TWITTER_AUTH:
    SOCIALACCOUNT_PROVIDERS['twitter'] = {
        'APP': {
            'client_id': TWITTER_ID,
            'secret': TWITTER_SECRET,
            'key': ''
        }
    }

SITE_ID = 1
