"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '41(lx+t+%hg!@cj$!gcjd&6=5e+l@c!))o*-u-i@+sux@k64-('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# IP Webserver
WEBSERVER = env.str('WEBSERVER', default='')

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    # https://www.django-rest-framework.org/#installation
    'rest_framework',
    # http://www.tomchristie.com/rest-framework-2-docs/api-guide/authentication#tokenauthentication
    'rest_framework.authtoken',
    # http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#extensions
    'django_celery_beat',
]
if DEBUG:
    THIRD_PARTY_APPS += [
        # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
        'debug_toolbar',
        'django_extensions',
    ]

# Apps specific for this prest_frameworkroject go here.
LOCAL_APP = [
    'mvc.apps.MVCConfig',
    'iot.apps.IOTConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APP
# https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = 'mvc.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
if DEBUG:
    MIDDLEWARE += [
        # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('POSTGRES_DB', default=''),
        'USER': env.str('POSTGRES_USER', default=''),
        'PASSWORD': env.str('POSTGRES_PASSWORD', default=''),
        'HOST': env.str('POSTGRES_HOST', default=''),
        'PORT': env.str('POSTGRES_PORT', default=''),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = env.str('TIME_ZONE', default='UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

# https://www.django-rest-framework.org/#installation
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}

# https://www.revsys.com/tidbits/celery-and-django-and-docker-oh-my/
CELERY_BROKER_URL = env.str('CELERY_BROKER_URL', default='')
CELERY_RESULT_BACKEND = env.str('CELERY_RESULT_BACKEND', default='')
CELERY_ACCEPT_CONTENT = env.list('CELERY_ACCEPT_CONTENT', str, default=[])
CELERY_TASK_SERIALIZER = env.str('CELERY_TASK_SERIALIZER', default='')
CELERY_RESULT_SERIALIZER = env.str('CELERY_RESULT_SERIALIZER', default='')

if DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'sql': {
                '()': 'utils.logging.SQLFormatter',
                'format': '[%(duration).3f] %(statement)s',
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            },
            'sql': {
                'class': 'logging.StreamHandler',
                'formatter': 'sql',
                'level': 'DEBUG',
            },
        },
        'loggers': {
            'django.db.backends': {
                'handlers': ['sql'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'django.db.backends.schema': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            },
        }
    }
