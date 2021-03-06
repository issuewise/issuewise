from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from locations.models.base import BaseLocation, BaseLocationGroup
from locations.utils import user_as_creator_factory
from core.utils import uri_name_mixin_factory

## Get appropriate mixin classes from their respective 
# factory methods.

UserAsCreatorClass = user_as_creator_factory(accounts_version_label = 'latest',
                                             core_version_label = 'latest')
UriNameMixinClass = uri_name_mixin_factory(version_label = 'latest')
                                                               

class WiseLocation(BaseLocation, UserAsCreatorClass, UriNameMixinClass):
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

    def clean(self):
        if not self.id:
            UriNameMixinClass.clean(self)

    def save(self,*args,**kwargs):    
        """
        Prior to saving, checks if the instance is being saved for the 
        first time in the database. If yes, cleans the name field
        and populates the uri_name field based on the cleaned name.
        """
        WiseLocation.full_clean(self)
        super(WiseLocation,self).save(*args,**kwargs)


    class Meta:
        app_label = 'locations'


class WiseLocationGroup(BaseLocationGroup, UserAsCreatorClass, UriNameMixinClass):

    def clean(self):
        if not self.id:
            UriNameMixinClass.clean(self)
    
    def save(self,*args,**kwargs):    
        """
        Prior to saving, checks if the instance is being saved for the 
        first time in the database. If yes, cleans the name field
        and populates the uri_name field based on the cleaned name.
        """
        WiseLocationGroup.pre_save_process(self)
        super(WiseLocationGroup,self).save(*args,**kwargs)


    class Meta:
        app_label = 'locations'


class LocationGroupMembership(models.Model):

    location_group = models.ForeignKey(settings.LOCATION_GROUP_MODEL,
        related_name = 'members', verbose_name = _('location group'))

    member = models.ForeignKey(settings.LOCATION_MODEL,
        related_name = 'location_group', verbose_name = _('member locations'))


    class Meta:
        app_label = 'locations'

    
    
