"""
This is the settings file used by developer Dibya Chakravorty.
You can use this as a template to create your custom settings file.
To use this settings file, use

python manage.py runserver --settings=issuewise.settings.dev_DC
"""

from .base import *

# Load SECRET_KEY as a system environment variable. This
# is done to ensure that the key remains secret.

SECRET_KEY = get_environment_variable('ISSUEWISE_SECRET_KEY')

# Database settings for MySQL server running on localhost

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'issuewise',
        'USER' : 'dibya',
        'PASSWORD' : get_environment_variable('POSTGRES_USER_PASSWORD'),
        'HOST' : 'localhost',
        'PORT': '',
    }
}




# All media files will stay under this directory

MEDIA_ROOT = BASE_DIR.ancestor(2).child('issuewise-media')

# Sub directory under MEDIA_ROOT/avatars for storing avatars of 
# different models. Keys should be in lowercase only. 
# ModelName should be written as modelname for example.

MODEL_AVATAR_DIR = {
    'accounts.wiseuser' : 'accounts/wiseusers',
    'groups.wisegroup' : 'groups/wisegroups',
    }
    
    
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'    
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'dibyachakravorty@gmail.com'
EMAIL_HOST_PASSWORD = get_environment_variable('MY_GMAIL_PASSWORD')
EMAIL_PORT = 587