from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from accounts.models.mixins import creatable_factory
from core.models import uri_name_mixin_factory

CreatableClass = creatable_factory()
UriNameMixinClass = uri_name_mixin_factory()


class BaseWiseGroup(CreatableClass):
    """
    ANY CUSTOM GROUP CLASS SHOULD INHERIT THIS MODEL

    Makes the following assumptions that are likely to hold in 
    the future:

    1. Groups have names, this is a required field
    2. Groups can be created by authenticated users
    3. Groups have members who are users
    """ 
    name = models.CharField(max_length=200, help_text=_('Required. ' 
        '200 characters or less.'), verbose_name=_('group name'))
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, 
        through=settings.GROUP_MEMBERSHIP_MODEL, 
        verbose_name=_('group members'))

    class Meta:
        abstract=True


class WiseGroup(BaseWiseGroup, UriNameMixinClass):
    """ Issuewise groups """
    
    def save(self,*args,**kwargs):
        if not self.id:
            self.clean_name()
            self.uri_name = WiseGroup.uri_name_manager.get_uri_name(self.name)
        super(WiseGroup,self).save(*args,**kwargs)

