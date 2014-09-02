'''

This is the settings file used by developer Dibya Chakravorty.
You can use this as a template to create your custom settings file.
To use this settings file, use

python manage.py runserver --settings=issuewise.settings.dev_DC

'''

from .base import *

# Load SECRET_KEY as a system environment variable. This
# is done to ensure that the key remains secret.

SECRET_KEY = get_environment_variable('ISSUEWISE_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

TEMPLATE_DEBUG = True

# Database settings for MySQL server running on localhost

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
		'NAME' : 'issuewise',
		'USER' : 'root',
		'PASSWORD' : get_environment_variable('MYSQL_ROOT_PASSWORD'),
		'HOST' : '127.0.0.1',
		'PORT': '3306',
    }
}
