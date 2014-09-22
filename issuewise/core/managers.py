import re
from django.db import models
from django.utils.http import urlquote


class UriNameManager(models.Manager):

    def get_uri_name(self,name):
        """
        Determines and returns an unique URI identifier for the given 
        name. Separating whitespaces are stripped and replaced with "-". 
        Rest of the characters are encoded.

        Any trailing whitespaces at the beginning or end of name
        should be stripped before calling this function.
        """
        name=re.sub(r"\s+",'-',name)
        uri_name=urlquote(name)
        count=self.filter(uri_name=uri_name).count()
        if count!=0:
            joined_name = u'-'.join([name, unicode(count)])
            uri_name=urlquote(joined_name)
        return uri_name
