from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class LocationAsTag(models.Model):
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


class LocationAsAddress(models.Model):
    
    location = models.ForeignKey(settings.LOCATION_MODEL,
        related_name = '%(app_label)s_%(class)s_set', 
        verbose_name = _('belongs to location'))
    line_1 = models.CharField(_('address line 1'), max_length = 50)
    line_2 = models.CharField(_('address line 2'), max_length = 50,
        null = True, blank = True)
    line_3 = models.CharField(_('address line 3'), max_length = 50,
        null = True, blank = True)
    zipcode = models.CharField(_('postal code'), max_length = 15)
    is_primary_address = models.BooleanField(_('is this the primary address?'),
        default = False)


    class Meta:
        abstract = True
        app_label = 'locations'


class LocationGroupAsTag(models.Model):

    location_group = models.ForeignKey(settings.LOCATION_GROUP_MODEL,
        related_name = '%(app_label)s_%(class)s_set',
        verbose_name = _('location group'))

    class Meta:
        abstract = True
