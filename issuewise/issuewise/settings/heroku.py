"""
This is the settings file used for deploying the app on Heroku.

Ensure that you set the environment variable DJANGO_SETTINGS_MODULE to 
issuewise.settings.production before deploying.
"""

from .base import *

# Load SECRET_KEY as a system environment variable. This
# is done to ensure that the key remains secret.

SECRET_KEY = get_environment_variable('ISSUEWISE_SECRET_KEY')

# Database settings for POSTGRES database for Heroku
# Parse database configuration from $DATABASE_URL

import dj_database_url

DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Set the domain name to the heroku app

DOMAIN_NAME = 'https://limitless-caverns-8697.herokuapp.com'


# setting DEBUG to False leads to unexpected behavior for DJANGO REST 
# FRAMEWORK's frontend