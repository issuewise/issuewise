from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class PageAsReference(models.Model):
    
    page = models.ForeignKey(settings.PAGE_MODEL,
        related_name = '%(app_label)s_%(class)s_set', 
        verbose_name = _('page'),
        null = True, blank = True)

    page_status = models.BooleanField(_('any Issuewise page matching '
        'matching this entry?'), default = False)

    page_name = models.CharField(_('name of the person/group'),
        max_length = 200, null = True, blank = True)

    description = models.TextField(_("description of the user's "
        "activities while at, and any continuing relations, with the user/group"),
        null = True, blank = True)

    is_current = models.BooleanField(_('is the user currently involved ' 
        'with this user/group'), default = False)

    
    class Meta:
        abstract = True
        app_label = 'pages'

