import re

from django.db import models
from django.utils.http import urlquote
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
    degeneracy = models.PositiveIntegerField()

    uri_name_manager=UriNameManager()

    class Meta:
        abstract = True

    def clean_name(self):
        """
        Any trailing whitespaces at the beginning or end of name
        are stripped 
        """
        self.name = re.sub(r"^\s+|\s+$",'',self.name)

    def get_uri_name(self, max_degeneracy):
        self.name=re.sub(r"\s+",'-',self.name)
        uri_name=urlquote(self.name)
        if max_degeneracy != -1:
            new_degeneracy_value = max_degeneracy + 1
            joined_name = u'-'.join([uri_name, unicode(new_degeneracy_value)])
            uri_name=urlquote(joined_name)
        self.uri_name = uri_name

    @classmethod
    def pre_save_process(cls, instance):
        if not instance.id:
            instance.clean_name()
            max_degeneracy = instance.__class__.uri_name_manager.get_name_max_degeneracy(instance.name)
            instance.get_uri_name(max_degeneracy)
            instance.degeneracy = max_degeneracy + 1
            
            
            




    

    
