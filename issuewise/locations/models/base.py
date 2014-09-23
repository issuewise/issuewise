from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.utils import hierarchy_factory

## Get appropriate mixin classes from their respective 
# factory methods.

HierarchyClass=hierarchy_factory(version_label = 'latest')

LOCATION_TYPE_CHOICES = (
    ('CO', 'Country'),
    ('ST', 'State/Province'),
    ('CI', 'City/Town/Village'),
    ('GL', 'Global'),
)


class BaseLocation(HierarchyClass):
    """
    ANY CUSTOM LOCATION MODEL SHOULD INHERIT FROM THIS MODEL

    Fields

    required : name

        Name of the category. No assumptions about characters allowed in 
        name.  Everything is allowed.

    required : location_type
    
        Political subdivision. Allowed values are
        - 'Country'
        - 'State/Province'
        - 'City/Town/Village'
        - 'Global' (means the planet Earth,
                    this is not really a political subdivision yet) 

    required : parent

        Refers to the parent division e.g a 'City' should refer to 
        a 'State', and a 'State' should refer to a 'Country'. Set to
        NULL if location_type = 'Global'.
    """
    
    name = models.CharField(_('location name'), max_length = 100)
    location_type = models.CharField(_('location type'), max_length = 50,
        choices = LOCATION_TYPE_CHOICES)

    
    class MPTTMeta:
        order_insertion_by = ['name']


    class Meta:
        app_label = 'locations'
        abstract = True
    
    
