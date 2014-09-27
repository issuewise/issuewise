from django.db import models
from django.conf import settings


class PublicCategoryAsTag(models.Model):
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


class GroupCategoryAsTag(models.Model):
    """ 
    ANY CUSTOM GROUPCATEGORYPLUG MODEL SHOULD INHERIT FROM
    THIS MODEL

    Fields
    
    required : category

        Denotes the category
    """
    group_category = models.ForeignKey(settings.GROUP_CATEGORY_MODEL,
        related_name='%(app_label)_%(class)_set',
        verbose_name=_('group_category'))

    class Meta:
        abstract = True



