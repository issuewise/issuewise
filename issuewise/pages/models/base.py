from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import ugettext_lazy as _


class BasePage(models.Model):
    
    content_type = models.ForeignKey(ContentType,
        verbose_name = _('model type'), null = True, blank = True)
    object_id = models.PositiveIntegerField(_('model primary key'),
        null = True, blank = True)
    content_object = GenericForeignKey('content_type', 'object_id')
    name = models.CharField(_('name of the page'), max_length = 200)


    class Meta:
        abstract = True
        app_label = 'pages'

