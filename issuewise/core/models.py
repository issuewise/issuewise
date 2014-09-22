import re
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from core.managers import UriNameManager

def uri_name_mixin_factory():
    """
    Factory method for the UriNameMixin model. If you extend the
    UriNameMixin model and want all your models to use the
    extended version, return it instead of UriNameMixin

    Any extension of UriNameMixin should extend from BaseUriNameMixin,
    otherwise things will break
    """
    return UriNameMixin


class BaseUriNameMixin(models.Model):
    """ 
    ANY URINAMEMIXIN CLASS SHOULD INHERIT FROM THIS MODEL

    Fields

    uri_name = NULL

        Denotes a URI name. Do not attempt to set this field yourself.
        You should always derive this from the model's 'name' field 
        by using the manager method 
        uri_mixin_manager.get_uri_name(name)

    Managers:

    core.managers.UriNameManger
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


class UriNameMixin(BaseUriNameMixin):
    """
    ADDS A 'uri_name' FIELD TO ANY MODEL THAT HAS A 'name' field
    THIS IS NOT A STANDALONE MODEL. BEFORE INHERITING, ENSURE
    THAT YOUR MODEL HAS A 'name' FIELD FOR THIS MODEL TO WORK.

    Fields
    
    required : uri_name

        see BaseUriNameMixin.uri_name

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

    class Meta:
        abstract = True


class Hierarchy(MPTTModel):
    """
    INHERIT THIS CLASS TO ESTABLISH A SELF HIERARCHIAL RELATIONSHIP 
    IN YOUR MODEL OR TO CREATE YOUR OWN CUSTOM HIERARCHY MIXIN

    Fields

    parent = NULL

        Denotes the immediate parent in the hierarchy of the 
        concrete model

    Usage:

        There are many ways to establish hierarchial relationships in
        a concrete model M. You might want to:
        
        - Inherit directly from MPTTModel and define a 'parent' field
          yourself. You should do this if the 'parent' field defined
          here is insufficient and requires additional customization

        - If the parent field defined here is sufficient, you can
          do one of the following depending on your need

            - If you need to add additional fields and methods
              related to hierarchy, make a mixin class which
              inherits Hierarchy and define all other customization
              in the mixin class. Then inherit the mixin
              in your model M. The mixin should precede any other 
              models that inherit models.Model in the inheritance chain 
              of M.

            - If no additional customization is required, and you 
              want to establish a bare basic hierarchy, simply inherit
              Hierarchy in your model M. Hierarchy should precede any 
              other models that inherit models.Model in the inheritance 
              chain of M.
    """
    parent = TreeForeignKey('self', null = True, blank = True,
        related_name = 'children')


    class Meta:
        abstract = True


    

    
