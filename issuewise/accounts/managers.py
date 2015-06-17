import re
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

from userprofile.models import WiseUserProfile

class CustomUserManager(BaseUserManager):
    """
    Manager for the BaseWiseUser abstract class. Any class
    that extends BaseWiseUser will receive this Manager as
    'objects'
    """

    def _create_user(self, name, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with a url_name,
        name, email and additional optional arguments.
        """
        now=timezone.now()
        if not name:
            raise ValueError('The full name must be set')
        if not email:
            raise ValueError('The email must be set')
        user = self.model(name=name,
                          email=email, is_staff=is_staff,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name, email, 
                    password=None, **extra_fields):
        """ 
        creates user with is_superuser = False and
        is_staff = False
        """
        return self._create_user(name, email, password, 
                                 False, False, **extra_fields)

    def create_superuser(self, name, 
                         email, password, **extra_fields):
        """
        creates user with is_superuser = True and
        is_staff = True
        """
        return self._create_user(name, email, password, 
                                 True, True, **extra_fields)


class WiseUserManager(CustomUserManager):
    """ This is the custom Manager for WiseUser. Extends CustomUserManager"""

    def create_user(self, *args, **kwargs):
        user = super(WiseUserManager, self).create_user(*args, **kwargs)
        WiseUserProfile.objects.create(autobiographer = user, privacy = 'F')
        return user
        
    def create_superuser(self, *args, **kwargs):
        user = super(WiseUserManager, self).create_superuser(*args, **kwargs)
        WiseUserProfile.objects.create(autobiographer = user, privacy = 'F')
        return user
        

    
    
    
class WiseFriendshipManager(models.Manager):

    def check_friendship(self, userA, userB):
        try:
            self.get(followee = userA, follower = userB, status = 'F')
            return True
        except self.model.DoesNotExist:
            return False
            
    def get_friend_list(self, user):
        return self.filter(followee = user, status = 'F')
        
    def get_total_friends(self, user):
        return self.filter(followee = user, status = 'F').count()
        
    def is_mutual_friend(self, userA, userB, userC):
        '''
        userC is the mutual friend of userA and userB
        '''
        if self.check_friendship(userA, userC) and self.check_friendship(userB, userC):
            return True
        return False
        
    def get_total_mutual_friends(self, userA, userB):
        friendlist = self.get_friend_list(userA)
        l = []
        for entry in friendlist:
            if self.is_mutual_friend(userA, userB, entry.follower):
                l.append(entry.id)
        return len(l)
        
        
    
            
       
    
