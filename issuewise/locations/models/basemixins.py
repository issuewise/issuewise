from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class BaseLocationPlug(models.Model):
    """
    ANY CUSTOM LOCATIONPLUG MODEL SHOULD INHERIT THIS MODEL

    Fields:

    required : location

        Denotes the lowest subdivision of the location. E.g if the
        location is Kolkata, West Bengal, India, Earth, simply
        set this to Kolkata.

    start = NULL
        
        Start date of this location association

    end = NULL
    
        End date of this location association
    """


    location = models.ForeignKey(settings.LOCATION_MODEL,
        related_name = '%(app_label)s_%(class)s_set',
        verbose_name = _('location'))


    class Meta:
        app_label = 'locations'
        abstract = True
