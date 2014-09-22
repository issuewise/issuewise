from django.db import models
from accounts.models.mixins import creatable_factory
from core.models import Hierarchy, uri_name_mixin_factory
from django.utils.translation import ugettext_lazy as _

## Get appropriate mixin classes from their respective 
# factory methods.

CreatableClass = creatable_factory()
UriNameMixinClass = uri_name_mixin_factory()

LOCATION_TYPE_CHOICES = (
    ('CO', 'Country'),
    ('ST', 'State/Province'),
    ('CI', 'City/Town/Village'),
    ('GL', 'Global'),
)


class BaseWiseLocation(Hierarchy):
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
        abstract = True


class WiseLocation(BaseLocation, CreatableClass, UriNameMixinClass):
    """
    ISSUEWISE LOCATION CLASS

    required : name
        
        see BaseLocation.name.
        All trailing whitespaces are removed when the WiseGroup 
        object is saved to the database for the first time.

    required : location_type

        see BaseLocation.location_type

    required : parent

        see BaseLocation.parent
    
    creator = NULL

        Denotes the user who created this location.Set to NULL when 
        the user is deleted.

    auto : created_at
    
        Denotes the time this location was created

    auto : uri_name

        Each Location gets a correctly encoded 'uri_name' field. 
        The uri_name appears in the URI as shown below: 
        issuewise.org/location/r'[(ancestor_type/ancestor_uri_name)+]'
        /location_type/location_uri_name
        This name is automatically assigned when the Location 
        object is saved to the database for the first time.
    """

    def save(self,*args,**kwargs):    
        """
        Prior to saving, checks if the instance is being saved for the 
        first time in the database. If yes, cleans the name field
        and populates the uri_name field based on the cleaned name.
        """
        if not self.id:
            self.clean_name()
            self.uri_name = Location.uri_name_manager.get_uri_name(self.name)
        super(Location,self).save(*args,**kwargs)

    
    
