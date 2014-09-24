from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core import validators

from core.utils import uri_name_mixin_factory
from accounts.models.base import BaseUser
from accounts.managers import WiseUserManager

# Get appropriate mixin classes from their respective 
# factory methods.

UriNameMixinClass = uri_name_mixin_factory(version_label = 'latest')


class WiseUser(BaseUser, UriNameMixinClass):
    """
    ISSUEWISE USERS

    Fields

    auto : uri_name

        Each user gets a correctly encoded uri_name. The uri_name
        appears in the user URI as shown below:
        issuewise.org/users/wiseuser_uri_name
        This name is automatically assigned when the WiseUser object 
        is saved to the database for the first time.

    required : name

        see BaseUser.name 
        All trailing whitespaces are removed when the WiseUser object 
        is saved to the database for the first time.

    required : email
        
        see BaseUser.email
        Email is normalized when the WiseUser object 
        is saved to the database for the first time.

    is_active = False

        Denotes whether the user account is active or inactive. 
        The account might be inactive for the following reasons:
        - email not verified
        - account deleted
        - account banned etc. 
    """
    is_active = models.BooleanField(_('active'), default=False,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    wise_user_manager=WiseUserManager()
    
    class Meta(BaseUser.Meta):
        app_label = 'accounts'

    def save(self,*args,**kwargs):
        """
        Prior to saving, checks if the instance is being saved for the 
        first time in the database. If yes, cleans the name field,
        populates the uri_name field based on the cleaned name and
        normalizes email.
        """
        if not self.id:
            self.email = WiseUser.objects.normalize_email(self.email)
        UriNameMixinClass.pre_save_process(self)
        super(WiseUser,self).save(*args,**kwargs)



    
