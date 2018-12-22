"""
Django settings for ecosmeticos project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY','123')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


ADMINS = (
    ('Cristiano', 'admecosmeticos@gmail.com'),
)
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#libs
    'widget_tweaks',
    'easy_thumbnails',
    'paypal.standard.ipn',
    #'watson',
#app
    'core',
    'accounts',
    'catalog',
    'checkout',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'checkout.middleware.cart_item_middleware',
]

ROOT_URLCONF = 'ecosmeticos.urls'

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
                # apps
                'catalog.context_processors.categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecosmeticos.wsgi.application'
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'WhiteNoise.storage.CompressedManifestStaticFilesStorage'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'pt_br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

##
#db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(db_from_env)
##
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')
##
ALLOWED_HOSTS = ['*']
##
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'staticfiles')
#STATIC_ROOT = os.path.join(BASE_DIR), 'staticfiles'
#MEDIA_ROOT = os.path.join(BASE_DIR), 'media'
MEDIA_ROOT = os.path.join(BASE_DIR), 'media'

#E-email
#EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER = 'admecosmeticos'
EMAIL_HOST_PASSWORD = ''
DEFAULD_FROM_EMAIL = 'admecosmeticos@gmail.com'

#auth
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_URL = 'logout'
AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = {
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.ModelBackend',
}

# Messages
from django.contrib.messages import constants as messages_constants
MESSAGE_TAGS = {
    messages_constants.DEBUG: 'debug',
    messages_constants.INFO: 'info',
    messages_constants.SUCCESS: 'success',
    messages_constants.WARNING: 'warning',
    messages_constants.ERROR: 'danger',
}

PAGSEGURO_TOKEN = ''
PAGSEGURO_EMAIL = 'admecosmeticos@gmail.com'
PAGSEGURO_SANDBOX = True

PAYPAL_TEST = True
PAYPAL_EMAIL = 'admecosmeticos@gmail.com'

# Thumbnail
THUMBNAIL_ALIASES = {
    '': {
        'product_image': {'size': (285, 160), 'crop': True},
    },
}

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'checkout.views': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'filename': os.path.join(BASE_DIR, 'pagseguro.log'),
        }
    },
    'loggers': {
        'views': {
            'handlers': ['checkout.views'],
            'level': 'DEBUG',
        }
    }
}



try:
    from .local_settings import *
except ImportError:
    pass
