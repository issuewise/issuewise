from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class BaseUserProfile(models.Model):
    """ 
    USER PROFILE MODEL
        
    Field

    required : user
        Denotes the user
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile',
                                verbose_name=_('user'))

    class Meta:
        abstract = True
        app_label = 'userprofile'
