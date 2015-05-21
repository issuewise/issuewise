from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework import permissions

from accounts.models import WiseFriendship
from issuewise.utils import get_model_from_settings

def permission_factory(view):

    if view in settings.PROFILE_PERMISSION_VIEW_CLASSES:
        return ProfilePermissions
    if view in settings.FRIENDSHIP_PERMISSION_VIEW_CLASSES:
        return FriendshipPermissions


class ProfilePermissions(object):

    @classmethod
    def is_permitted(cls, request, model, obj, url_capture):
        if obj:
            owner = obj.owner()
            if request.method in permissions.SAFE_METHODS:
                if obj.privacy == 'A':  
                    return True
                friends = WiseFriendship.objects.check_friendship(request.user,owner)
                if friends:
                    return True
            return owner == request.user
        user_model = get_model_from_settings(settings.AUTH_USER_MODEL)   
        owner = get_object_or_404(user_model , uri_name = url_capture['uri_name'])
        return owner == request.user
        
 
class FriendshipPermissions(object):
 
    @classmethod
    def is_permitted(cls, request, model, obj, url_capture):
        user_model = get_model_from_settings(settings.AUTH_USER_MODEL)   
        owner = get_object_or_404(user_model , uri_name = url_capture['uri_name'])
        if request.method in permissions.SAFE_METHODS:
            friends = WiseFriendship.objects.check_friendship(request.user,owner)
            if friends:
                return True
            return owner == request.user
        if request.method == 'PUT':
            return owner == request.user
        if request.method == 'DELETE':
            return owner == request.user
        return True
           
            
         
        
           
            