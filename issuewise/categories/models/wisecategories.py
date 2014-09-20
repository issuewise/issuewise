from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from accounts.models.mixins import creatable_factory
from core.models import uri_name_mixin_factory
from groups.models.mixins import owned_by_group_factory

CreatableClass = creatable_factory()
UriNameMixinClass = uri_name_mixin_factory()
OwnedByGroupClass = owned_by_group_factory()


class BaseCategory(CreatableClass):
    """ Categories are used to label other objects. 
    Any model that inherits this class behaves like a category. """ 
    name = models.CharField(_('category name'), max_length=50)

    class Meta:
        abstract = True


class PublicCategory(BaseCategory, UriNameMixinClass):
    """ Categories in the public domain """

    def save(self,*args,**kwargs):
        if not self.id:
            self.clean_name()
            self.uri_name = PublicCategory.uri_name_manager.get_uri_name(self.name)
        super(PublicCategory,self).save(*args,**kwargs)


class GroupCategory(BaseCategory, UriNameMixinClass, OwnedByGroupClass):
    """ Categories that are owned by groups """

    def save(self,*args,**kwargs):
        if not self.id:
            self.clean_name()
            self.uri_name = GroupCategory.uri_name_manager.get_uri_name(self.name)
        super(GroupCategory,self).save(*args,**kwargs)

