from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail


from core.utils import (uri_name_mixin_factory, activity_mixin_factory,
                        user_as_follower_factory, user_as_followee_factory,
                        user_as_creator_factory)

from accounts.models.base import BaseUser
from accounts.managers import WiseUserManager, WiseFriendshipManager

from pages.utils import page_as_reference_factory


# Get appropriate mixin classes from their respective 
# factory methods.

UriNameMixinClass = uri_name_mixin_factory(version_label = 'latest')
ActivityMixinClass = activity_mixin_factory(version_label = 'latest')
UserAsFollowerClass = user_as_follower_factory(version_label = 'latest')
UserAsFolloweeClass = user_as_followee_factory(version_label = 'latest')
UserAsCreatorClass = user_as_creator_factory(version_label = 'latest')


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

    auto : degeneracy

        Denotes the degeneracy for the given Full name in the 
        database at the time of creation.  

    required : name

        see BaseUser.name 
        All trailing whitespaces are removed when the WiseUser object 
        is saved to the database for the first time.

    required : email
        
        see BaseUser.email
        Email is normalized when the WiseUser object 
        is saved to the database for the first time.

    activity_status = 'inactive'

        Denotes whether the user account is 'active' or 'inactive'.
        For allowed options, see WiseUser.ACTIVITY_STATUS

    activity_status_explanation = 'NV' ('not verified')
     
        Explanation for the current activity status. For allowed 
        options, see WiseUser.ACTIVITY_STATUS_EXPLANATION

    auto : status changed

        Stores the date and time when the field activity_status 
        last changed.
    """

    ACTIVITY_STATUS = (
        ('I', 'inactive'), #default
        ('A', 'active'),
    )

    ACTIVITY_STATUS_EXPLANATION = (
        ('NE', 'no explanation'),#default
        ('NV', 'not verified'), 
        ('AB', 'account blocked'),
        ('AD', 'account deactivated'),
    )

    objects=WiseUserManager()
    
    def owner(self):
        return self
    
    
    def send_activation_email(self):
        unique_code = unicode(uuid4())
        activation_link = ''.join([settings.DOMAIN_NAME, '/users'])
        activation_link = ''.join([activation_link, '/activation-links/'])
        activation_link = ''.join([activation_link, unique_code])
        # why is my email id in this line?
        send_mail('activate your issuewise account', 
            ''.join(['your activation link is ' , activation_link]), 'dibyachakravorty@gmail.com',
            [self.email], fail_silently=False)
        WiseActivation.objects.create(uuid = unique_code, creator = self)
        
    def send_password_reset_email(self):
        unique_code = unicode(uuid4())
        activation_link = ''.join([settings.DOMAIN_NAME, '/users'])
        activation_link = ''.join([activation_link, '/password-reset-links/'])
        activation_link = ''.join([activation_link, unique_code])
        send_mail('your password reset link', 
            ''.join(['your password reset link is ' , activation_link]), 'dibyachakravorty@gmail.com',
            [self.email], fail_silently=False)
        WisePasswordReset.objects.create(uuid = unique_code, creator = self)
        
    def activate(self):
        self.activity_status = 'A'
        self.explanation = 'NE'
        self.save()
        for link in WiseActivation.objects.filter(creator = self):
            link.delete()
        
        
        
        
    
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


    class Meta(BaseUser.Meta):
        app_label = 'accounts'
        
        
STATUS_CHOICES = (
    ('F', 'Friends'),
    ('R', 'Friend Request Sent'),
)        


class WiseFriendship(UserAsFollowerClass, UserAsFolloweeClass):  

    objects = WiseFriendshipManager()

    UserAsFollowerClass.follower.help_text = _('This is one of the users \
        in the friendship relation. If the status of the friendship is R \
        (request sent), this field indicates the person who sent the request')
    
    UserAsFolloweeClass.followee.help_text = _('This is one of the users \
        in the friendship relation. If the status of the friendship is R \
        (request sent), this field indicates the person who received the request')
    
    status = models.CharField(_('friendship status'), max_length = 5,
        choices = STATUS_CHOICES, null = True, blank = True,
        help_text = _('Status of the friendship relation. This could be \
        R denoting Request Sent or this could be F meaning that the users \
        are already friends.'))
    
    class Meta:
        app_label = 'accounts'
        unique_together = (('follower', 'followee'),)
        
        
    
class Activation(UserAsCreatorClass):
    
    uuid = models.CharField(_('unique id'), max_length = 100)
    
    class Meta:
        app_label = 'accounts'
        abstract = True
     
class WiseActivation(Activation):

     class Meta:
        app_label = 'accounts'
        
        
class WisePasswordReset(Activation):

     class Meta:
        app_label = 'accounts'



    