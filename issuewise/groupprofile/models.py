from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class GroupProfile(models.Model):
    """ 
    GROUP PROFILE MODEL
        
    Field

    required : group
        Denotes the group
    """
    group = models.OneToOneField(settings.SITE_GROUP_MODEL, related_name='profile',
                                verbose_name=_('group'))
