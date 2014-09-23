from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from groups.models.base import BaseGroup, BaseMembership
from core.utils import uri_name_mixin_factory
from groups.utils import group_hierarchy_factory

# Get appropriate mixin classes from their respective 
# factory methods.

UriNameMixinClass = uri_name_mixin_factory(version_label = 'latest')
GroupHierarchyClass = group_hierarchy_factory(version_label = 'latest')


class WiseGroup(GroupHierarchyClass, BaseGroup, UriNameMixinClass):
    """ 
    ISSUEWISE GROUPS 
    
    auto : uri_name

        Each WiseGroup gets a correctly encoded 'uri_name' field. 
        The uri_name appears in the URI as shown below: 
        issuewise.org/groups/wisegroup_uri_name
        This name is automatically assigned when the WiseGroup 
        object is saved to the database for the first time.

    required : name

        see BaseGroup.name
        All trailing whitespaces are removed when the WiseGroup 
        object is saved to the database for the first time.

    creator = NULL
    
        see BaseGroup.creator
    """
    
    def save(self,*args,**kwargs):
        """
        Prior to saving, checks if the instance is being saved for the 
        first time in the database. If yes, cleans the name field
        and populates the uri_name field based on the cleaned name.
        """
        if not self.id:
            self.clean_name()
            self.uri_name = WiseGroup.uri_name_manager.get_uri_name(self.name)
        super(WiseGroup, self).save(*args,**kwargs)

    class Meta:
        app_label = 'groups'


class WiseMembership(BaseMembership):
    """
    GROUP MEMBERSHIP CLASS
    
    Fields

    required : group
        Denotes the group. Subscription is deleted when the group 
        deleted

    required : subscriber
        Denotes the member (user). Subscription is deleted when
        the user gets deleted

    auto : subscribed_at
        Denotes the time at which the user became a member of the
        group
    """
    class Meta:
        app_label = 'groups'

