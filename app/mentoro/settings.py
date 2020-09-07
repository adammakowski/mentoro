import os
# SENTRY SDK - Django and Redis https://sentry.io
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://b5618401fa044fc1b952aa8677600a7a@o376411.ingest.sentry.io/5197194", integrations=[DjangoIntegration()],
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = int(os.environ.get("DEBUG", default=0))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# Django Debug Toolbar https://github.com/jazzband/django-debug-toolbar
INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
    '0.0.0.0',
]
# Show Debug Toolbar in Docker
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
}

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_registration',  # https://django-registration.readthedocs.io
    'captcha',  # https://github.com/praekelt/django-recaptcha
    'ckeditor',  # https://github.com/django-ckeditor/django-ckeditor
    'ckeditor_uploader',  # https://github.com/django-ckeditor/django-ckeditor#required-for-using-widget-with-file-upload
    'django_extensions',  # https://github.com/django-extensions/django-extensions
    'crispy_forms',  # https://django-crispy-forms.readthedocs.io
    'optimized_image',  # TinyPNG optimize images
    'defender',  # https://django-defender.readthedocs.io/en/latest/
    'debug_toolbar',  # Django Debug Toolbar https://github.com/jazzband/django-debug-toolbar
    'simple_history',  # https://django-simple-history.readthedocs.io
    'django_cleanup.apps.CleanupConfig',  # https://github.com/un1t/django-cleanup
    'django_drf_filepond',  # https://django-drf-filepond.readthedocs.io/en/latest/
    'anymail',  # https://anymail.readthedocs.io/en/stable/
    'home',  # home app
    'accounts',  # accounts app
    'dashboard',  # dashboard app
    'courses',  # Mentoro|Courses app
    'library',  # Mentoro|Library app
    'mentors',  # Mentoro|Mentors app
    'experts',  # Mentoro|Experts app
    'blog',  # Mentoro|Blog app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # Django Debug Toolbar https://github.com/jazzband/django-debug-toolbar
    'simple_history.middleware.HistoryRequestMiddleware',  # https://django-simple-history.readthedocs.io
    'defender.middleware.FailedLoginMiddleware',  # https://django-defender.readthedocs.io/en/latest/
]

ROOT_URLCONF = 'mentoro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

WSGI_APPLICATION = 'mentoro.wsgi.application'

# Caches Redis
CACHES = {
    "default": {
        "BACKEND": os.environ.get("REDIS_BACKEND"),
        "LOCATION": os.environ.get("REDIS_LOCATION"),
        "OPTIONS": {
            "CLIENT_CLASS": os.environ.get("REDIS_CLIENT_CLASS"),
            "COMPRESSOR": os.environ.get("REDIS_COMPRESSOR"),
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    },
    "pool1": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE_POOL1", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
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

# Password Hasher Argon2
# https://docs.djangoproject.com/en/3.0/topics/auth/passwords/#using-argon2-with-django

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'staticfiles/'),)
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'staticfiles')
STATICFILES_FINDERS = ('django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder',)
MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

# STORAGE AWS S3 - files and staticfiles
if DEBUG:
    STATIC_URL = '/staticfiles/'
else:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_S3_CUSTOM_DOMAIN')
    AWS_S3_REGION_NAME = 'eu-central-1'
    AWS_DEFAULT_ACL = None
    AWS_IS_GZIPPED = True
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_S3_ADDRESSING_STYLE = 'virtual'
    # s3 static settings
    AWS_LOCATION = 'staticfiles'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# URLS
LOGIN_REDIRECT_URL = 'dashboard_index'

# Email config Mailgun SMTP
EMAIL_BACKEND = "anymail.backends.sendinblue.EmailBackend"
DEFAULT_FROM_EMAIL = "support@mentoro.online"  # if you don't already have this in settings
ANYMAIL = {
    "SENDINBLUE_API_KEY": "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",
}

# Django reCaptcha
RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")

# TinyPNG compress images
OPTIMIZED_IMAGE_METHOD = 'tinypng'
TINYPNG_KEY = os.environ.get("TINYPNG_KEY")

# Django Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

#  Django Defender
# https://django-defender.readthedocs.io/en/latest/
DEFENDER_REDIS_URL = os.environ.get("REDIS_LOCATION")
DEFENDER_LOGIN_FAILURE_LIMIT = 4
DEFENDER_LOCK_OUT_BY_IP_AND_USERNAME = True
DEFENDER_LOCKOUT_URL = 'account_locked'

#  django-registration - https://django-registration.readthedocs.io/en/3.1
ACCOUNT_ACTIVATION_DAYS = 1  # One-day activation window
REGISTRATION_OPEN = True

# Filepond JS Uploader
# https://django-drf-filepond.readthedocs.io/en/latest/
if DEBUG:
    DJANGO_DRF_FILEPOND_UPLOAD_TMP = os.path.join(BASE_DIR, 'filepond-temp-uploads')
    DJANGO_DRF_FILEPOND_FILE_STORE_PATH = os.path.join(BASE_DIR, 'stored_uploads')
else:
    DJANGO_DRF_FILEPOND_STORAGES_BACKEND = 'storages.backends.s3boto3.S3Boto3Storage'

# Ckeditor Uploader
CKEDITOR_UPLOAD_PATH = os.path.join(BASE_DIR, 'ckeditor-uploads')
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%'
    },
}
