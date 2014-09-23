from django.db import models
from django.utils.translation import ugettext_lazy as _

from locations.models.base import BaseLocation
from locations.utils import creatable_factory
from core.utils import uri_name_mixin_factory

## Get appropriate mixin classes from their respective 
# factory methods.

CreatableClass = creatable_factory(accounts_version_label = 'latest',
                                   core_version_label = 'latest')
UriNameMixinClass = uri_name_mixin_factory(version_label = 'latest')


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
        super(WiseLocation,self).save(*args,**kwargs)


    class Meta:
        app_label = 'locations'

    
    
