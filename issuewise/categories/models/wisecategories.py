from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from categories.models.base import BaseCategory
from core.utils import uri_name_mixin_factory
from groups.utils import owned_by_group_factory

# Get appropriate mixin classes from their respective 
# factory methods.

UriNameMixinClass = uri_name_mixin_factory(version_label = 'latest')
OwnedByGroupClass = owned_by_group_factory(version_label = 'latest')


class WisePublicCategory(BaseCategory, UriNameMixinClass):
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
        UriNameMixinClass.pre_save_process(self)
        super(WisePublicCategory,self).save(*args,**kwargs)

    class Meta: 
        app_label = 'categories'
        verbose_name = 'public category'
        verbose_name_plural = 'public categories'


class WiseGroupCategory(BaseCategory, UriNameMixinClass, OwnedByGroupClass):
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
        UriNameMixinClass.pre_save_process(self)
        super(WiseGroupCategory,self).save(*args,**kwargs)

    class Meta:
        app_label = 'categories'
        verbose_name = 'group category'
        verbose_name_plural = 'group categories'

