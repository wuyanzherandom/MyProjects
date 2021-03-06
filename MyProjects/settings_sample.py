# -*- coding: utf-8 -*-
"""
Django settings for myprojects project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=ze(1$e(5j+31o#pxr_bf!lxo@fj=py4-g7*7j=dsq1hyzfs%j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if not DEBUG:
    ALLOWED_HOSTS = ['45.118.133.135', 'www.animedex.tk', 'animedex.tk']
else:
    ALLOWED_HOSTS = []

INTERNAL_IPS = '127.0.0.1'

ADMINS = (
    ('mono', 'monomono2354@gmail.com'),
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mainmailsend@gmail.com'
EMAIL_HOST_PASSWORD = 'monday123'
EMAIL_PORT = 587
#EMAIL_HOST_USER = 'support@animenetunit.com'
#EMAIL_HOST_PASSWORD = 'monday123'
DEFAULT_FROM_EMAIL = 'support@animenetunit.com'
SERVER_EMAIL = 'support@manimenetunit.com'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myprojects.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'projects.animenet.context_processors.global_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'myprojects.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     'animenet',
        'USER':     'postgres',
        'PASSWORD': 'monday123',
        'HOST':     '127.0.0.1',
        'PORT':     '5433'
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#MEMCACHE_HOST = ['127.0.0.1:11211']


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

USE_TZ = False

TIME_ZONE = 'Asia/Kuala_Lumpur'

LANGUAGES = (
    ('en', 'English'),
    ('zh-hans', u'中文'),
    ('th', u'ภาษา')
)

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 24 * 60 * 60
SESSION_SAVE_EVERY_REQUEST = True

LANGUAGE_COOKIE_NAME = 'lang'
LANGUAGE_COOKIE_AGE = 726122880
#LANGUAGE_COOKIE_PATH = '/'
#LANGUAGE_COOKIE_DOMAIN = None

#CSRF_FAILURE_VIEW = 'projects.django_common_feature._views.csrf_failure'
CSRF_COOKIE_HTTPONLY = True

CACHE_KEY_PREFIX = 'myprojects.'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(message)s'
        },
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django-debug-log.log')
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['logfile'],  #'mail_admins', 'logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

CACHE = False
if CACHE:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            #'BACKEND': 'memcachepool.cache.UMemcacheCache',
            'LOCATION': '127.0.0.1:11211',
            'KEY_PREFIX': CACHE_KEY_PREFIX,
        }
    }
    """
    'TIMEOUT': 300,
    'OPTIONS': {
        'MAX_POOL_SIZE': 35,
        'BLACKLIST_TIME': 20,
        'SOCKET_TIMEOUT': 5,
        'MAX_ITEM_SIZE': 1000*1000,
    }
    """
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"

#CACHE_MIDDLEWARE_ALIAS =
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_KEY_PREFIX = CACHE_KEY_PREFIX


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

INSTALLED_APPS += [
    'projects.animenet',
]

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]


from projects_settings.base_projects import *
from projects_settings.animenet import *