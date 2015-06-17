from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import permissions

from accounts.models import WiseFriendship
from issuewise.utils import get_model_from_settings

def permission_factory(view):

    if view in settings.PROFILE_PERMISSION_VIEW_CLASSES:
        return ProfilePermissions
    if view in settings.FRIENDSHIP_PERMISSION_VIEW_CLASSES:
        return FriendshipPermissions
        
        
class Relationship(object):

    @classmethod
    def request_type(cls, request, obj, owner):
        # permission classes for this family
        
        friends = WiseFriendship.objects.check_friendship(request.user,owner)
        if friends:
            request_type ='friend'
        elif owner == request.user:
            request_type = 'owner'
        else:
            request_type = 'stranger'
        print request_type    
        return request_type

    


class ProfilePermissions(Relationship):


    @classmethod
    def is_permitted(cls, request, obj, owner):
        
        request_type= cls.request_type(request, obj, owner)
        
        if obj:
            if request.method in permissions.SAFE_METHODS:
                if obj.privacy == 'A':  
                    return True
                elif request_type == 'friend':
                    return True
                elif request_type == 'owner':
                    return True
                return False
        return owner == request.user
        
 
class FriendshipPermissions(Relationship):
 
    @classmethod
    def is_permitted(cls, request, obj, owner ):
    
        request_type= cls.request_type(request, obj, owner)
            
        # method wise permission assignment
        
        if request.method in permissions.SAFE_METHODS:
            if request_type == 'friend':
                return True
            elif request_type == 'stranger':
                if WiseFriendship.objects.is_mutual_friend(owner, request.user, obj.follower):
                    return True
                return False 
            elif request_type =='owner':
                return True 
            return False
        if request.method == 'PUT':
            if request_type == 'owner':
                return True
            return False
        if request.method == 'DELETE':
            if request_type == 'owner':
                return True
            return False
        if request.method == 'POST':
            if request_type == 'owner':
                return False
            return True
           
            
         
        
           
            