from django.db import models
from django.conf import settings

from categories.models.basemixins import BasePublicCategoryPlug, BaseGroupCategoryPlug


class WisePublicCategoryPlug(BasePublicCategoryPlug):
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
        app_label = 'categories'


class WiseGroupCategoryPlug(BaseGroupCategoryPlug):
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
        app_label = 'categories'

