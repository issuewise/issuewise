from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

def owned_by_group_factory():
    return OwnedByGroup


class BaseOwnedByGroup(models.Model):
    """
    Any model that can be owned by a group should inherit this
    class
    """
    owner = models.ForeignKey(settings.SITE_GROUP_MODEL,
        related_name='category_set',
        verbose_name=_('group which owns this category')) 
    
    class Meta:
        abstract = True


class OwnedByGroup(BaseOwnedByGroup):

    class Meta:
        abstract = True
