from django.db import models
from django.conf import settings

def public_category_plug_factory():
    """
    Factory method for the PublicCategoryPlug model. If you extend the
    PublicCategoryPlug model and want all your models to use the
    extended version, return it instead of PublicCategoryPlug

    Any extension of PublicCategoryPlug should extend from 
    BasePublicCategoryPlug, otherwise things will break
    """
    return PublicCategoryPlug

def group_category_plug_factory():
    """
    Factory method for the GroupCategoryPlug model. If you extend the
    GroupCategoryPlug model and want all your models to use the
    extended version, return it instead of GroupCategoryPlug

    Any extension of GroupCategoryPlug should extend from 
    BaseGroupCategoryPlug, otherwise things will break
    """
    return GroupCategoryPlug


class BasePublicCategoryPlug(models.Model):
    """ 
    ANY CUSTOM PUBLICCATEGORYPLUG MODEL SHOULD INHERIT FROM
    THIS MODEL

    Fields
    
    required : category

        Denotes the category
    """
    category = models.ForeignKey(settings.PUBLIC_CATEGORY_MODEL,
        related_name='%(app_label)_%(class)_set',
        verbose_name=_('category'))

    class Meta:
        abstract = True


class PublicCategoryPlug(BasePublicCategoryPlug):
    """
    THIS CLASS IS USED TO LABEL PUBLIC OBJECTS WITH CATEGORIES

    Fields

    required : category

        see BasePublicCategoryPlug.category

    Additional info:

        To label public objects with categories, do the following:

        - Create a mixin model that has a ManyToManyField which
            points to settings.PUBLIC_CATEGORY_MODEL

        - If the many to many relation requires additional fields,
            then use "through" in the ManyToManyField to reference a
            custom join model

        - Inherit PublicCategoryPlug in the "through" model using
          public_category_plug_factory

        - Inherit the mixin model in the model that needs labeling
    """
    
    class Meta:
        abstract = True


class BaseGroupCategoryPlug(models.Model):
    """ 
    ANY CUSTOM GROUPCATEGORYPLUG MODEL SHOULD INHERIT FROM
    THIS MODEL

    Fields
    
    required : category

        Denotes the category
    """
    category = models.ForeignKey(settings.GROUP_CATEGORY_MODEL,
        related_name='%(app_label)_%(class)_set',
        verbose_name=_('category'))

    class Meta:
        abstract = True


class GroupCategoryPlug(BaseGroupCategoryPlug):
    """
    THIS CLASS IS USED TO LABEL GROUP OBJECTS WITH CATEGORIES

    Fields

    required : category

        see BaseGroupCategoryPlug.category

    Additional info:

        To label group objects with categories, do the following:

        - Create a mixin model that has a ManyToManyField which
            points to settings.GROUP_CATEGORY_MODEL

        - If the many to many relation requires additional fields,
            then use "through" in the ManyToManyField to reference a
            custom join model

        - Inherit GroupCategoryPlug in the "through" model using
          group_category_plug_factory

        - Inherit the mixin model in the model that needs labeling
    """

    class Meta:
        abstract = True

