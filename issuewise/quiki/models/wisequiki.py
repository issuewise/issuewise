from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from quiki.models.base import BaseQuiki, BaseNobit
from core.utils import user_as_creator_factory, user_as_moderator_factory

UserAsCreatorClass = user_as_creator_factory(version_label = 'latest')
UserAsModeratorClass = user_as_moderator_factory(version_label = 'latest')


class Quiki(BaseQuiki):
    
    class Meta:
        app_label = 'quiki'


FLAG_CHOICES = (
    ('G', 'Grammar and Spelling'),
)


class Nobit(BaseNobit, UserAsCreatorClass, UserAsModeratorClass):

    flag = models.CharField(_('flag applied by moderator'), 
        max_length = 255, null = True, choices = FLAG_CHOICES)
    comment = models.TextField(_('comment made by moderator'),
        null = True)

    class Meta:
        app_label = 'quiki'
    
