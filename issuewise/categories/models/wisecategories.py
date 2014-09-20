from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from accounts.models.mixins import Creatable
from core.models import UriNameMixin
from groups.models.mixins import OwnedByGroup


class BaseCategory(Creatable):
    """ Categories are used to label other objects. 
    Any model that inherits this class behaves like a category. """ 
    name = models.CharField(_('category name'), max_length=50)

    class Meta:
        abstract = True


class PublicCategory(BaseCategory, UriNameMixin):
    """ Categories in the public domain """

    def save(self,*args,**kwargs):
        if not self.id:
            self.clean_name()
            self.uri_name = PublicCategory.uri_name_manager.get_uri_name(self.name)
        super(PublicCategory,self).save(*args,**kwargs)


class GroupCategory(BaseCategory, UriNameMixin, OwnedByGroup):
    """ Categories that are owned by groups """

    def save(self,*args,**kwargs):
        if not self.id:
            self.clean_name()
            self.uri_name = GroupCategory.uri_name_manager.get_uri_name(self.name)
        super(GroupCategory,self).save(*args,**kwargs)


class PublicCategoryPlug(models.Model):
    """ 
    This is a plug for the PublicCategory model. Any entity
    that needs to be labeled with a PublicCategory should do the 
    following:

    1. Create a mixin model that has a ManyToManyField which
    points to settings.PUBLIC_CATEGORY_MODEL.

    2. If the many to many relation requires additional fields,
    then use "through" in the ManyToManyField to reference a
    custom join model.

    3.. Inherit PublicCategoryPlug in the "through" model.

    4. Inherit the mixin model in the model that needs labeling.
    """
    category = models.ForeignKey(settings.PUBLIC_CATEGORY_MODEL,
        related_name='%(app_label)_%(class)_set',
        verbose_name=_('category'))

    class Meta:
        abstract=True


class GroupCategoryPlug(models.Model):
    """ This is a plug for the GroupCategory model. Any entity
    that needs to be labeled with a GroupCategory should do the 
    following:

    1. Create a mixin model that has a ManyToManyField which
    points to settings.GROUP_CATEGORY_MODEL.

    2. If the many to many relation requires additional fields,
    then use "through" in the ManyToManyField to reference a
    custom join model.

    3.. Inherit GroupCategoryPlug in the "through" model.

    4. Inherit the mixin model in the model that needs labeling.
    """
    category = models.ForeignKey(settings.GROUP_CATEGORY_MODEL,
        related_name='%(app_label)_%(class)_set',
        verbose_name=_('category'))

    class Meta:
        abstract=True


