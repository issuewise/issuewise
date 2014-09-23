from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from groups.utils import creatable_factory, subscribable_factory 

# Get appropriate mixin classes from their respective 
# factory methods.

CreatableClass = creatable_factory(accounts_version_label = 'latest',
                                   core_version_label = 'latest')
SubscribableClass = subscribable_factory(accounts_version_label = 'latest',
                                           core_version_label = 'latest')


class BaseGroup(CreatableClass):
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
        app_label = 'groups'
        abstract=True


class BaseMembership(SubscribableClass):
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
    group = models.ForeignKey(settings.SITE_GROUP_MODEL,
        verbose_name=_('group'), related_name = '%(app_label)s_%(class)s_set')


    class Meta:
        app_label = 'groups'
        abstract = True

