from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from subscription.models import Subscription


class WiseGroup(models.Model):
	""" Issuewise groups """
	creator = models.OneToOneField(settings.AUTH_USER_MODEL,
                                   related_name='creator', null=True, 
                                   on_delete=models.SET_NULL, 
                                   verbose_name=_('creator'))
	creation_datetime = models.DateTimeField(_('date created'), auto_now_add=True)
	name = models.CharField(max_length=200, help_text=_('Required. ' 
                            '200 characters or less.'), verbose_name=_('group name'))
	members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Membership',
                                     verbose_name=_('group members'))


class Membership(Subscription):
	wisegroup = models.ForeignKey(settings.SITE_GROUP_MODEL,
                                  verbose_name=_("group"))
