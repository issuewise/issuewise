from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class GroupAsOwner(models.Model):
    """
    ANY CUSTOM OWNEDBYGROUP MODEL SHOULD INHERIT FROM THIS CLASS

    Fields

    required : owner

        Denotes the owner (group) of an object. Any object owned by a
        group will be deleted when the group is deleted  
    """
    owner = models.ForeignKey(settings.SITE_GROUP_MODEL,
        related_name = '%(app_label)s_%(class)s_set',
        verbose_name = _('owner'))

    
    class Meta:
        app_label = 'groups'
        abstract = True


class GroupAsAutobiographer(models.Model):

    autobiographer = models.ForeignKey(settings.SITE_GROUP_MODEL,
        related_name = '%(app_label)s_%(class)s_set',
        verbose_name = _('group'))

    
    class Meta:
        app_label = 'groups'
        abstract = True
