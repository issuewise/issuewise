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

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

TEMPLATE_DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '4%hom^_1re&=f^e-0k9t5ribs^x+teukn(j_cj((7#wck$z4-8'

# A list of strings representing the host/domain names that this 
# Django site can serve. This is a security measure to prevent an 
# attacker from poisoning caches and password reset emails with links 
# to malicious hosts by submitting requests with a fake HTTP Host 
# header, which is possible even under many seemingly-safe web server 
# configurations. Host name validation is disabled if debug is set to 
# TRUE.

ALLOWED_HOSTS = ['www.issuewise.org']

# Database configuration. Set to use sqlite3.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME' : BASE_DIR.child('issuewise.db'),
    }
}

DOMAIN_NAME = 'http://127.0.0.1:8000'

SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_version': '0.1',
    'api_path': '/',
    'enabled_methods': [
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    'api_key': '',
    'is_authenticated': False,
    'is_superuser': False,
    'permission_denied_handler': None,
    'info': {
        'contact': 'dibyachakravorty@gmail.com',
        'description': 'This is the issuewise API, which is currently under \
development.',
        'message' : 'edit society',
        'title': 'issuewise',
    },
    'doc_expansion': 'none',
}


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'core',
    'accounts',
    'userprofile',
    'groups',
    'categories',
    'groupprofile',
    'locations',
    'avatars',
    'pages',
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


#REST_FRAMEWORK = {
#    'DEFAULT_AUTHENTICATION_CLASSES': (
#        'rest_framework.authentication.TokenAuthentication',
#    )
#}

ROOT_URLCONF = 'issuewise.urls'

WSGI_APPLICATION = 'issuewise.wsgi.base.application'


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
        
        
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'    
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = get_environment_variable('MY_EMAIL_ID')
EMAIL_HOST_PASSWORD = get_environment_variable('MY_EMAIL_PASSWORD')
EMAIL_PORT = 587

# Model declarations

# To avoid hardcoding your models, use
# from django.conf import settings
# ...and then use settings.APPROPRIATE_MODEL
# to establish Foreign Key relationships and for other purposes.

# Custom models for users

AUTH_USER_MODEL = 'accounts.WiseUser'
FRIENDSHIP_MODEL = 'accounts.WiseFriendship'
PASSWORD_RESET_LINK_MODEL = 'accounts.WisePasswordReset'
ACTIVATION_LINK_MODEL = 'accounts.WiseActivation'

# Custom models for groups

SITE_GROUP_MODEL = 'groups.WiseGroup'
GROUP_MEMBERSHIP_MODEL = 'groups.Membership'

# Custom models for categories

PUBLIC_CATEGORY_MODEL = 'categories.WisePublicCategory'
GROUP_CATEGORY_MODEL = 'categories.WiseGroupCategory'

# Custom models for locations

LOCATION_MODEL = 'locations.WiseLocation'
LOCATION_GROUP_MODEL = 'locations.WiseLocationGroup'
LOCATION_GROUP_MEMBERSHIP_MODEL = 'locations.LocationGroupMembership'

# Custom models for userprofile

USER_PROFILE_MODEL = 'userprofile.WiseUserProfile'
SOCIAL_LINK_MODEL = 'userprofile.UserSocialLink'

# Custom models for groupprofile

GROUP_PROFILE_MODEL = 'groupprofile.WiseGroupProfile'

# Custom models for pages

PAGE_MODEL = 'pages.WisePage'

# Custom models for Quiki

#QUIKI_MODEL = 'quiki.Quiki'
#NOBIT_MODEL = 'quiki.Nobit'

# Many to many relationship models (join tables)

BATCH_MODEL = 'userprofile.Batch'

# All media files will stay under this directory

MEDIA_ROOT = BASE_DIR.child('media')

# Sub directory under MEDIA_ROOT/avatars for storing avatars of 
# different models. Keys should be in lowercase only. 
# ModelName should be written as modelname for example.

MODEL_AVATAR_DIR = {
    'accounts.wiseuser' : 'users',
    'groups.wisegroup' : 'groups',
    }

# Avatar thumbnail size settings

THUMBNAIL_HEIGHT = 40
THUMBNAIL_WIDTH = 40

PROFILE_PERMISSION_VIEW_CLASSES = (
                                    'PersonalInfo',
                                    'EduInsListCreate',
                                    'ActivationLinkCheck',
                                    'ActivationLinkCreate',
                                    'SocialLinkList',
                                    'SocialLinkDetail',
                                    'Profile',
                                    )
                                    
FRIENDSHIP_PERMISSION_VIEW_CLASSES = (
                                        'FriendshipList',
                                        'AcceptRejectFriend',
                                        )