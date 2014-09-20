from django.db import models
from django.conf import settings


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

