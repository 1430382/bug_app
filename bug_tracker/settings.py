"""
Django settings for bug_tracker project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from data_project import *
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'bootstrap_modal_forms',
    # 'django_user_agents',
    'bug_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'bug_tracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [''],
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

WSGI_APPLICATION = 'bug_tracker.wsgi.application'


TARGET_ENV = 'dev'
try:
  TARGET_ENV = os.environ["TARGET_ENV"]
except:
  pass
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

if TARGET_ENV == "dev":
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    #localhost
    DB_NAME = 'bug_tracker'
    DB_USER = 'bug_trackeruser'
    DB_PASS = '.bug.'
    DB_HOST = ''
    DB_PORT = ''
elif TARGET_ENV == "prod":
    ## SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False
    ##Produccion
    #DB_NAME = ''
    #DB_USER = ''
    #DB_PASS = ''
    #DB_HOST = ''
    #DB_PORT = ''

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql', 
        'NAME':     DB_NAME,           
        'USER':     DB_USER,
        'PASSWORD': DB_PASS,
        'HOST':     DB_HOST,                       
        'PORT':     DB_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/bug_tracker.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'django.template': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        # 'autentificacion': {
        #     'handlers': ['file'],
        #     'level': 'DEBUG',
        # },
        # apps logger
        'bug_app': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        #'modelos': {
        #    'handlers': ['file'],
        #    'level': 'DEBUG',
        #},
        # system logger
        'bug_tracker': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}
