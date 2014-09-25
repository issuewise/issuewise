from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from groups.models.basemixins import BaseOwnedByGroup
from core.utils import hierarchy_factory

HierarchyClass = hierarchy_factory(version_label = 'latest')


class WiseGroupHierarchy(HierarchyClass):
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
    is_spokesgroup = models.BooleanField(_('represents the parent group'),
        default = False) 
    
    class Meta:
        app_label = 'groups'
        abstract = True
