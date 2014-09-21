from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from accounts.models.mixins import creatable_factory
from core.models import uri_name_mixin_factory

# Get appropriate mixin classes from their respective 
# factory methods.

CreatableClass = creatable_factory()
UriNameMixinClass = uri_name_mixin_factory()


class BaseWiseGroup(CreatableClass):
    """
    ANY CUSTOM GROUP CLASS SHOULD INHERIT THIS MODEL

    Fields

    required : name
        
        Name of the category. No assumptions about characters allowed in 
        name.  Everything is allowed.

    creator = NULL

        User who created this group. Set to NULL when the user
        is deleted.
    """ 
    name = models.CharField(max_length=200, help_text=_('Required. ' 
        '200 characters or less.'), verbose_name=_('group name'))
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, 
        through=settings.GROUP_MEMBERSHIP_MODEL, 
        verbose_name=_('group members'))

    class Meta:
        abstract=True


class WiseGroup(BaseWiseGroup, UriNameMixinClass):
    """ 
    ISSUEWISE GROUPS 
    
    auto : uri_name

        Each WiseGroup gets a correctly encoded 'uri_name' field. 
        The uri_name appears in the URI as shown below: 
        issuewise.org/groups/wisegroup_uri_name
        This name is automatically assigned when the WiseGroup 
        object is saved to the database for the first time.

    required : name

        see BaseWiseGroup.name
        All trailing whitespaces are removed when the WiseGroup 
        object is saved to the database for the first time.

    creator = NULL
    
        see BaseWiseGroup.creator
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
        super(WiseGroup,self).save(*args,**kwargs)

    class Meta:
        app_label = 'groups'

