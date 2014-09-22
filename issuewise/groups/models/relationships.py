from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from accounts.models.mixins import subscribable_factory

# Get appropriate mixin classes from their respective 
# factory methods.

SubscribableModel = subscribable_factory()


class Membership(SubscribableModel):
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
        verbose_name=_('group'))


    class Meta:
        app_label = 'groups'
    
