from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _


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
        related_name = 'children', verbose_name = _('parent'))


    class Meta:
        abstract = True

