import re
from django.db import models


class UriNameManager(models.Manager):

    def get_name_max_degeneracy(self,name):
        """
        Determines and returns an unique URI identifier for the given 
        name. Separating whitespaces are stripped and replaced with "-". 
        Rest of the characters are encoded.

        Any trailing whitespaces at the beginning or end of name
        should be stripped before calling this function.
        """
        degeneracy_set=self.filter(name=name)
        if degeneracy_set.exists():
            max_degeneracy = degeneracy_set.aggregate(models.Max('degeneracy'))['degeneracy__max']
        else:
            max_degeneracy = -1
        return max_degeneracy
