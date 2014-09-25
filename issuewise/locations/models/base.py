from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.utils import hierarchy_factory

## Get appropriate mixin classes from their respective 
# factory methods.

HierarchyClass = hierarchy_factory(version_label = 'latest') 

LOCATION_TYPE_CHOICES = (
    ('COU', 'Country'),
    ('AD1', 'Primary administrative division'),
    ('AD2', 'Secondary administrative division'),
    ('AD3', 'Tertiary administrative division'),
    ('CIT', 'Major populated region like cities/towns/villages'),
    ('SUB', 'Suburban regions'), 
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
    location_type = models.CharField(_('offcial location type defined '
                                       'by geographic databases'), 
                                     max_length = 50,
                                     choices = LOCATION_TYPE_CHOICES)
    colloquial_location_type = models.CharField(('colloquial location type'),
                                                max_length = 50)

    
    class MPTTMeta:
        order_insertion_by = ['name']


    class Meta:
        app_label = 'locations'
        abstract = True


SUPERLOCATION_TYPE_CHOICES = (
    ('CON', 'Continents'),
    ('MIL', 'Military'),
    ('ECO', 'Economic'),
    ('HEA', 'Healthcare'),
    ('ENV', 'Environmental'),
    ('EDU', 'Educational'),
    ('LAN', 'Language'),
    ('PEA', 'Peace/Conflict Resolution'),
    ('REG', 'Regional'),
    ('CUL', 'Cultural'),
    ('ETH', 'Ethnic'),
    ('REL', 'Religious'),
    ('HIS', 'Historical'),
    ('AID', 'Humanitarian Aid'),
    ('OTH', 'Others'),
)


class BaseSuperLocation(models.Model):

    name = models.CharField(_('superlocation name'), max_length = 200)
    alliance_type = models.CharField(_('alliance type'), 
                                     max_length = 60, null = True, blank = True,
                                     choices = SUPERLOCATION_TYPE_CHOICES)

    class Meta:
        abstract = True
        app_label = 'locations'
    
    
