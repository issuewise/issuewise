from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from locations.models.basemixins import BaseLocationPlug

class WiseLocationPlug(BaseLocationPlug):
    """
    THIS PLUG MAY BE USED TO ESTABLISH MANY TO ONE OR 
    MANY TO MANY RELATIONSHIPS WITH THE LOCATION MODEL 
    settings.LOCATION_MODEL

    Fields

    required : location

        see BaseLocation.location

    start = NULL
        
        Start date of this location association

    end = NULL
    
        End date of this location association

    Additional info:

        Do the following to establish a many to many relationship
        with your model M and the your location model

        - Create a mixin model M' that has a ManyToManyField which
          points to settings.LOCATION_MODEL

        - If the many to many relation requires additional fields,
          then use "through" in the ManyToManyField to reference a
          custom join model

        - Inherit LocationPlug in the "through" model using 
          location_plug_factory

        - Inherit the mixin model M' in the model M

        To establish a many to one relationship from your model
        to the location model, simply inherit LocationPlug using
        location_plug_factory in your model
    """

    start = models.DateField(blank = True, null = True)
    end = models.DateField (blank = True, null =True)


    class Meta:
        app_label = 'locations'
        abstract = True
