from django.db import models
from django.utils.translation import ugettext_lazy as _


class StartEndDate(models.Model):

    start = models.DateField(_('start date'))
    end = models.DateField(_('end_date'))

    
    class Meta:
        abstract = True
