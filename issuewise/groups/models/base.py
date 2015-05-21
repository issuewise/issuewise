from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from groups.utils import user_as_creator_factory

# Get appropriate mixin classes from their respective 
# factory methods.

UserAsCreatorClass = user_as_creator_factory(accounts_version_label = 'latest',
                                             core_version_label = 'latest')


class BaseGroup(UserAsCreatorClass):
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

    class Meta:
        app_label = 'groups'
        abstract=True

