from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from accounts.models.mixins import creatable_factory
from core.models import uri_name_mixin_factory
from groups.models.mixins import owned_by_group_factory

# Get appropriate mixin classes from their respective 
# factory methods.

CreatableClass = creatable_factory()
UriNameMixinClass = uri_name_mixin_factory()
OwnedByGroupClass = owned_by_group_factory()


class BaseCategory(CreatableClass):
    """ 
    CATEGORIES ARE USED TO LABEL OTHER OBJECTS.
    ANY CUSTOM CATEGORY CLASS SHOULD INHERIT THIS MODEL  
    
    Field

    required : name
    
        Name of the category. No assumptions about characters allowed in 
        name.  Everything is allowed.

    creator = NULL

        User who created this category. Set to NULL when the user
        is deleted.

    auto : created_at
        Time at which the group was created.
    """ 
    name = models.CharField(_('category name'), max_length=50)

    class Meta:
        abstract = True


class PublicCategory(BaseCategory, UriNameMixinClass):
    """ 
    THIS IS A CLASS FOR CATEGORIES IN THE PUBLIC DOMAIN

    Fields

    auto : uri_name

        Each PublicCategory gets a correctly encoded 'uri_name' field. 
        The uri_name appears in the URI as shown below: 
        issuewise.org/categories/public_category_uri_name
        This name is automatically assigned when the PublicCategory 
        object is saved to the database for the first time.

    required : name

        see BaseCategory.name
        All trailing whitespaces are removed when the PublicCategory 
        object is saved to the database for the first time.

    creator = NULL
    
        see BaseCategory.creator

    auto : created_at
        see BaseCategory.created_at
    """

    def save(self,*args,**kwargs):
        """
        Prior to saving, checks if the instance is being saved for the 
        first time in the database. If yes, cleans the name field
        and populates the uri_name field based on the cleaned name
        """
        if not self.id:
            self.clean_name()
            self.uri_name = PublicCategory.uri_name_manager.get_uri_name(self.name)
        super(PublicCategory,self).save(*args,**kwargs)

    class Meta: 
        app_label = 'categories'
        verbose_name = 'public category'
        verbose_name_plural = 'public categories'


class GroupCategory(BaseCategory, UriNameMixinClass, OwnedByGroupClass):
    """ 
    THIS IS A CLASS FOR CATEGORIES OWNED BY GROUPS

    Fields

    auto : uri_name

        Each GroupCategory gets a correctly encoded 'uri_name' field. 
        The uri_name appears in the URI as shown below: 
        issuewise.org/groups/wisegroup_uri_name/categories/group_category_uri_name
        This name is automatically assigned when the GroupCategory object 
        is saved to the database for the first time.

    required : name

        see BaseCategory.name
        All trailing whitespaces are removed when the GroupCategory 
        object is saved to the database for the first time.

    required : owner

        Denotes the group which owns the category. GroupCategory 
        database rows are deleted upon deletion of the owner group.

    creator = NULL
    
        see BaseCategory.creator

    auto : created_at
        see BaseCategory.created_at
    """

    def save(self,*args,**kwargs):
        """
        Prior to saving, checks if the instance is being saved for the 
        first time in the database. If yes, cleans the name field
        and populates the uri_name field based on the cleaned name.
        """
        if not self.id:
            self.clean_name()
            self.uri_name = GroupCategory.uri_name_manager.get_uri_name(self.name)
        super(GroupCategory,self).save(*args,**kwargs)

    class Meta:
        app_label = 'categories'
        verbose_name = 'group category'
        verbose_name_plural = 'group categories'

