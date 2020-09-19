"""
Base settings to build other setting files.
"""
import os
from pathlib import Path
import environ
from datetime import timedelta

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
APPS_DIR = BASE_DIR / "clinic"

env = environ.Env()

base = environ.Path(__file__) - 3
READ_DOT_ENV_FILE = base('.env')

if READ_DOT_ENV_FILE:
    env.read_env(READ_DOT_ENV_FILE)

DATABASES = {
    "default": env.db("DATABASE_URL", default="postgres:///clinic")
}

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

AUTH_USER_MODEL = 'staffs.Staff'

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'storages',
    'simple_history',
    'rest_framework',
    'corsheaders',
]

LOCAL_APPS = [
    "clinic.appointments",
    "clinic.locations",
    "clinic.machines",
    "clinic.patient_sessions.apps.PatientSessionsConfig",
    "clinic.patients",
    "clinic.procedures",
    "clinic.rooms",
    "clinic.staffs",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = str(BASE_DIR / "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(APPS_DIR / "static")]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Digital Ocean config
AWS_ACCESS_KEY_ID = env('BUCKET_ACCESS_KEY_ID',default='')
AWS_SECRET_ACCESS_KEY = env('BUCKET_SECRET_ACCESS_KEY',default='')

AWS_STORAGE_BUCKET_NAME = env('BUCKET_STORAGE_BUCKET_NAME',default='')
AWS_S3_ENDPOINT_URL = env('BUCKET_S3_ENDPOINT_URL',default='')
# If enabled the CDN, so you get a custom domain. Use the end point in the AWS_S3_CUSTOM_DOMAIN setting. 
AWS_S3_CUSTOM_DOMAIN = env('BUCKET_S3_CUSTOM_DOMAIN',default='')
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_DEFAULT_ACL = 'public-read'

DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

MEDIA_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, 'media')
MEDIA_ROOT = 'media/'


EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_TIMEOUT = 5

ADMIN_URL = "admin/"
ADMINS = [("""Daniel Roy Greenfeld""", "daniel-roy-greenfeld@example.com")]
MANAGERS = ADMINS

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),

    'AUTH_HEADER_TYPES': ('Bearer',),
}

# CORS_ALLOWED_ORIGINS = [
#     "http://192.168.1.8:8081"
#     "http://localhost:8081",
#     "http://127.0.0.1:8080"
# ]

CORS_ALLOW_ALL_ORIGINS = True