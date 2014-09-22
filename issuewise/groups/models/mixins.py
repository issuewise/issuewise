from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from core.models import Hierarchy

def owned_by_group_factory():
    """
    Factory method for the OwnedByGroup model. If you extend the
    OwnedByGroup model and want all your models to use the
    extended version, return it instead of OwnedByGroup

    Any extension of OwnedByGroup should extend from BaseOwnedByGroup,
    otherwise things will break
    """
    return OwnedByGroup

def group_hierarchy_factory():
    """
    Factory method for the GroupHierarchy model. If you extend the
    GroupHierarchy model and want all your models to use the
    extended version, return it instead of GroupHierarchy

    Any GroupHierarchy model should either extend from GroupHierarchy 
    or inherit Hierarchy, otherwise things will break
    """
    return GroupHierarchy


class BaseOwnedByGroup(models.Model):
    """
    ANY CUSTOM OWNEDBYGROUP MODEL SHOULD INHERIT FROM THIS CLASS

    Fields

    required : owner

        Denotes the owner (group) of an object. Any object owned by a
        group will be deleted when the group is deleted  
    """
    owner = models.ForeignKey(settings.SITE_GROUP_MODEL,
        related_name='category_set',
        verbose_name=_('group which owns this category')) 
    
    class Meta:
        abstract = True


class OwnedByGroup(BaseOwnedByGroup):
    """
    THIS IS USED TO CREATE A GROUP OWNER LIKE RELATIONSHIP

    Fields
    
    required : owner
        see BaseOwnedByGroup.owner
    
    Additional info:

        To make a model ownable by groups, inherit this class in 
        the model
    """
    class Meta:
        abstract = True


class GroupHierarchy(Hierarchy):
    """
    A GROUP HIERARCHY MIXIN.

    Fields
    
    parent = NULL

        see Hierarchy.parent

    Usage:
        
        To establish a hierarchial relationship in your group model,
        simply inherit this model using group_hierarchy_factory. This
        model should precede any other models that inherit models.Model
        in the inheritance chain of your group model
    """
    
    class Meta:
        abstract = True
