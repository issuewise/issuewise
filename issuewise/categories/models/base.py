from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from categories.utils import user_as_creator_factory

# Get appropriate mixin classes from their respective 
# factory methods.

UserAsCreatorClass = user_as_creator_factory(accounts_version_label = 'latest',
                                             core_version_label = 'latest')


class BaseCategory(UserAsCreatorClass):
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

