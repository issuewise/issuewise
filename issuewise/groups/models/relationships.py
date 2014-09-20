from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from accounts.models.mixins import Subscribable


class Membership(Subscribable):
    """
    While extending, only include functionality which assumes the 
    base class BaseWiseGroup.
    """
    group = models.ForeignKey(settings.SITE_GROUP_MODEL,
        verbose_name=_("group"))
