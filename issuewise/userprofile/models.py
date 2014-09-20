from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
    """ Stores additional information for users """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile',
                                verbose_name=_("user"))
