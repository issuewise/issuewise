"""
Base settings to be inherited by all other settings files. 

You are welcome to create your custom settings file. It is recommended 
that you keep your custom settings in the current directory. To import
the base settings to your custom settings file use 

from .base import * 
"""

import os

from django.core.exceptions import ImproperlyConfigured

from unipath import Path

# BASE_DIR points to the project root which is immediately below
# the repository root.
# Build your paths like this :
# PATH=BASE_DIR.child("first_child_dir", "second_child_dir") and so on

BASE_DIR = Path(__file__).absolute().ancestor(3)

# A list of strings representing the host/domain names that this 
# Django site can serve. This is a security measure to prevent an 
# attacker from poisoning caches and password reset emails with links 
# to malicious hosts by submitting requests with a fake HTTP Host 
# header, which is possible even under many seemingly-safe web server 
# configurations. Host name validation is disabled if debug is set to 
# TRUE.

ALLOWED_HOSTS = ['www.issuewise.org']


# Application definition
# accounts should always be the last app listed! 

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'userprofile',
    'groups',
    'categories',
    'accounts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'issuewise.urls'

WSGI_APPLICATION = 'issuewise.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


def get_environment_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

# Custom User model

AUTH_USER_MODEL = 'accounts.WiseUser'
SITE_GROUP_MODEL = 'groups.WiseGroup'
PUBLIC_CATEGORY_MODEL = 'categories.PublicCategory'
GROUP_CATEGORY_MODEL = 'categories.GroupCategory'





