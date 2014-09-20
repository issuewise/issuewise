import re
from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.managers import UriNameManager


class UriNameMixin(models.Model):
    """ Adds a uri_name field to any model that has a name field.
    If you want to include a uri_name field to a model, do the
    following:
    
    1. Inherit UriNameMixin in the model
        - the model will have a uri_name field
        - the model will have a manager : uri_name_manager
    2. Define a save method in your model which, among other things,
    should do the following in order the first time an instance is 
    saved:
        - strip trialing whitespaces from name
        - set uri_name using
          ModelClass.uri_name_manager.get_uri_name(name) 
    """
    uri_name = models.TextField(_('encoded uri name'), null = True)

    uri_name_manager=UriNameManager()

    class Meta:
        abstract = True

    def clean_name(self):
        """
        Any trailing whitespaces at the beginning or end of name
        are stripped 
        """
        self.name = re.sub(r"^\s+|\s+$",'',self.name)


    

    
