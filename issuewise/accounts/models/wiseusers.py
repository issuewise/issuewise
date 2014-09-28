from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _



from core.utils import (uri_name_mixin_factory, activity_mixin_factory,
                        user_as_follower_factory, user_as_followee_factory,
                        user_as_autobiographer_factory, social_link_factory)
from accounts.models.base import BaseUser
from accounts.managers import WiseUserManager
from pages.utils import page_as_reference_factory


# Get appropriate mixin classes from their respective 
# factory methods.

UriNameMixinClass = uri_name_mixin_factory(version_label = 'latest')
ActivityMixinClass = activity_mixin_factory(version_label = 'latest')
SocialLinkClass = social_link_factory(version_label = 'latest')
UserAsFollowerClass = user_as_follower_factory(version_label = 'latest')
UserAsFolloweeClass = user_as_followee_factory(version_label = 'latest')


class WiseUser(BaseUser, UriNameMixinClass, ActivityMixinClass):
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
    ACTIVITY_STATUS = (
        ('I', 'inactive'), #default
        ('A', 'active'),
    )

    ACTIVITY_STATUS_EXPLANATION = (
        ('NV', 'not verified'), #default
        ('AB', 'account blocked'),
        ('AD', 'account deleted'),
    )

    wise_user_manager=WiseUserManager()
    
    class Meta(BaseUser.Meta):
        app_label = 'accounts'

    def clean(self):
        if not self.id:
            self.email = WiseUser.objects.normalize_email(self.email)
            UriNameMixinClass.clean(self)

    def save(self,*args,**kwargs):
        """
        Prior to saving, checks if the instance is being saved for the 
        first time in the database. If yes, cleans the name field,
        populates the uri_name field based on the cleaned name and
        normalizes email.
        """
        WiseUser.full_clean(self)
        super(WiseUser,self).save(*args,**kwargs)


class UserFollowUser(UserAsFollowerClass, UserAsFolloweeClass):


    class Meta:
        app_label = 'accounts'
    




    
