import re

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.managers import UriNameManager

class UriNameMixin(models.Model):
    """ 
    ADDS A 'uri_name' FIELD TO ANY MODEL THAT HAS A 'name' field
    THIS IS NOT A STANDALONE MODEL. BEFORE INHERITING, ENSURE
    THAT YOUR MODEL HAS A 'name' FIELD FOR THIS MODEL TO WORK.

    Fields

    uri_name = NULL

        Denotes a URI name. Do not attempt to set this field yourself.
        You should always derive this from the model's 'name' field 
        by using the manager method 
        uri_mixin_manager.get_uri_name(name)

    Managers:

    core.managers.UriNameManger

    Usage:
        
        If you want to include a uri_name field to a model M, do the
        following:
    
        - Inherit UriNameMixin in the model using uri_name_mixin_factory
            -> the model will get a uri_name field
            -> the model will get a manager : uri_name_manager
    
        - Define a save method in your model which, among other things,
          should do the following in order the first time an instance 
          is saved to the database:
            - strip trialing whitespaces from name
            - set uri_name using
              M.uri_name_manager.get_uri_name(name)
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




    

    
