from django.http import Http404
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db import IntegrityError
from django.core.urlresolvers import reverse

from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from issuewise.utils import get_model_from_settings
from core.views import PermissionMixin, WiseListCreateAPIView, WiseRetrieveUpdateDestroyAPIView, WiseRetrieveUpdateAPIView
from core.serializers.social_link_serializers import SocialLinkSerializer
from accounts.models import WiseUser
from accounts.serializers import WiseFriendshipSerializer
from userprofile.models import WiseUserProfile
from userprofile.serializers import WiseUserProfileSerializer


class Profile(PermissionMixin,APIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    usermodel = get_model_from_settings(settings.AUTH_USER_MODEL)
    friendshipmodel = get_model_from_settings(settings.FRIENDSHIP_MODEL)
    
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(self.usermodel, uri_name = self.kwargs['uri_name'])
        uri_name = user.uri_name
        total_friends = self.friendshipmodel.objects.get_total_friends(user = user)
        response_dict = {
                        'username' : user.name,
                        'personal_info' : reverse('userprofile:personal-info',
                            kwargs = {'uri_name' : uri_name}),
                        'friend_list' : reverse('userprofile:friendshiplist',
                            kwargs = {'uri_name' : uri_name}),
                        'social_links' : reverse('userprofile:social-link-list',
                            kwargs = {'uri_name' : uri_name}),
                        'url' : reverse('userprofile:profile',
                            kwargs = {'uri_name' : uri_name}),
                        'total_friends' : total_friends,
                        }
        request_type = self.get_request_type(request, self.__class__.__name__,
            None, user)
        if request_type == 'stranger':
            response_dict['relation']='stranger'
            response_dict['friend_request']=reverse('userprofile:friendshiplist',
                            kwargs = {'uri_name' : uri_name})
            response_dict['friend_request_method'] = 'POST'
        else:
            response_dict['relation'] = request_type
        return Response(response_dict)
            
    
    


class PersonalInfo(PermissionMixin, WiseRetrieveUpdateAPIView):

    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = WiseUserProfileSerializer
        
    usermodel = get_model_from_settings(settings.AUTH_USER_MODEL)
    profilemodel = get_model_from_settings(settings.USER_PROFILE_MODEL)
    
    @property
    def owner(self):
        try:
            return self._owner
        except AttributeError:
            self._owner = get_object_or_404(self.usermodel, uri_name = self.kwargs['uri_name'])
            return self._owner
    
    def get_object(self):
        print 'bla'
        wiseuser = get_object_or_404(self.usermodel, uri_name = self.kwargs['uri_name'])
        obj = get_object_or_404(self.profilemodel, autobiographer = wiseuser)
        self.obj = obj
        return super(PersonalInfo, self).get_object()
        
    def get(self, request, *args, **kwargs):
        """
        
        Function : Get personal details of an user.
        
        Permission : Authenticated user only. The user himself or his friends
        are allowed access
        
        ---
        
        omit_parameters:
            - path 
            
        responseMessages:
            - code : 404
              message : This error occurs if the uri_name provided does not \
              correspond to a valid user on the system.
        
        """
        self.error_dict = {'stranger' : 'you do not have permission to view \
this information'}
        return super(PersonalInfo, self).get(request, *args, **kwargs) 
     
    def put(self, request, *args, **kwargs):
        """
        
        Function : Change personal details of an user.
        
        Permission : Authenticated user only. Only the user corresponding to 
        uri_name is allowed access.
        
        ---
        
        omit_parameters:
            - path
            
        responseMessages:
            - code : 404
              message : This error occurs if the uri_name provided does not \
              correspond to a valid user on the system.
            - code : 403
              message : This error occurs if the user making the request \
              is not the user corresponding to uri_name
        
        """
        self.error_dict = {'stranger' : 'you are not the owner of this resource. \
Therefore you cannot modify it' , 'friend' :  'you are not the owner of this resource. \
Therefore you cannot modify it'}
        return super(PersonalInfo, self).put(request, *args, **kwargs)
        
    
        
        
class SocialLinkList(PermissionMixin, WiseListCreateAPIView):
    
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = SocialLinkSerializer
    
    usermodel = get_model_from_settings(settings.AUTH_USER_MODEL)
    social_link_model = get_model_from_settings(settings.SOCIAL_LINK_MODEL)
    
    @property
    def owner(self):
        try:
            return self._owner
        except AttributeError:
            self._owner = get_object_or_404(self.usermodel, uri_name = self.kwargs['uri_name'])
            return self._owner
            
    def get_queryset(self):
        wiseuser = get_object_or_404(self.usermodel, uri_name = self.kwargs['uri_name'])
        links = self.social_link_model.objects.filter(autobiographer = wiseuser)
        self.qs = links
        return super(SocialLinkList, self).get_queryset()
        
    def perform_create(self, serializer):
        serializer.save(autobiographer=self.request.user)
        
    def get(self, request, *args, **kwargs):
        """
        
        Function : Lists the social media links of the user.  
        
        Permission : Authenticated user only. The user corresponding to the 
        uri_name and friends of the user are always allowed access. For non
        friends this node lists the social links that have privacy set to 
        A or public.         
        ---
        
        omit_parameters:
            - path
            
        
        responseMessages:
            - code : 404
              message : This error occurs if the uri_name provided does not \
              correspond to a valid user on the system.
        """
        
        return super(SocialLinkList, self).get(request, *args, **kwargs) 
        
    def post(self, request, *args, **kwargs):
        """
        
        Function : Creates a new social media link for the user corresponding 
        to the uri_name.  
        
        Permission : Authenticated user only. Only the user corresponding to 
        uri_name is allowed access.     
        ---
        
        omit_parameters:
            - path
            
        
        responseMessages:
            - code : 404
              message : This error occurs if the uri_name provided does not \
              correspond to a valid user on the system.
            - code : 403
              message : This error occurs if the user making the request \
              is the user corresponding to uri_name. 
        """
        self.error_dict = {'stranger' : 'you are not the owner of this resource. \
Therefore you cannot create a new resource here' , 'friend' :  'you are not the \
owner of this resource. Therefore you cannot create a new resource here'}
        return super(SocialLinkList, self).post(request, *args, **kwargs) 
        
        
        

class SocialLinkDetail(PermissionMixin, WiseRetrieveUpdateDestroyAPIView):

    
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = SocialLinkSerializer
    
    social_link_model = get_model_from_settings(settings.SOCIAL_LINK_MODEL)
    
    @property
    def owner(self):
        try:
            return self._owner
        except AttributeError:
            social_link = get_object_or_404(self.social_link_model, id = self.kwargs['pk'])
            obj = social_link
            self._owner = obj.autobiographer
            return self._owner
    
    def get_user(self):
        social_link = get_object_or_404(self.social_link_model, id = self.kwargs['pk'])
        return social_link.autobiographer
        
    
    def get_object(self):
        social_link = get_object_or_404(self.social_link_model, id = self.kwargs['pk'])
        self.obj = social_link
        return super(SocialLinkDetail, self).get_object()  
    
    
    def get(self, request, *args, **kwargs):
        """
        
        Function : Returns the social link corresponding to pk for the 
        user corresponding to uri_name 
        
        Permission : Authenticated user only. The user corresponding to the 
        uri_name and friends of the user are always allowed access. Non friends
        have access only if privacy is set to A or public.     
        ---
        
        omit_parameters:
            - path
            
        
        responseMessages:
            - code : 404
              message : This error occurs if the uri_name provided does not \
              correspond to a valid user on the system or if the user \
              corresponding to uri_name does not have a social link entry \
              corresponding to pk.
            - code : 403 
              message : This error occurs if a non friend is trying to \
              access a social link entry with privacy set to F
        """
        self.error_dict = {'stranger' : 'you do not have permission to view \
this information'}
        return super(SocialLinkDetail, self).get(request, *args, **kwargs) 
        
    def put(self, request, *args, **kwargs):
        """
        
        Function : Change the social link entry corresponding to pk of the 
        user corresponding to uri_name. 
        
        Permission : Authenticated user only. Only the user corresponding to 
        uri_name is allowed access.     
        ---
        
        omit_parameters:
            - path
            
        
        responseMessages:
            - code : 404
              message : This error occurs if the uri_name provided does not \
              correspond to a valid user on the system or if the user \
              corresponding to uri_name does not have a social link entry \
              corresponding to pk.
            - code : 403
              message : This error occurs if the user making the request \
              is not the user corresponding to uri_name
        """
        self.error_dict = {'stranger' : 'you are not the owner of this resource. \
Therefore you cannot modify it' , 'friend' :  'you are not the owner of this \
resource. Therefore you cannot modify it'}
        return super(SocialLinkDetail, self).post(request, *args, **kwargs) 
     
    def delete(self, request, *args, **kwargs):
        """
        
        Function : Delete the social link entry corresponding to pk of the 
        user corresponding to uri_name. 
        
        Permission : Authenticated user only. Only the user corresponding to 
        uri_name is allowed access.     
        ---
        
        omit_parameters:
            - path
            
        
        responseMessages:
            - code : 404
              message : This error occurs if the uri_name provided does not \
              correspond to a valid user on the system or if the user \
              corresponding to uri_name does not have a social link entry \
              corresponding to pk.
            - code : 403
              message : This error occurs if the user making the request \
              is not the user corresponding to uri_name
        """
        self.error_dict = {'stranger' : 'you are not the owner of this resource. \
Therefore you cannot delete it' , 'friend' : 'you are not the owner of this resource. \
Therefore you cannot delete it'}
        return super(SocialLinkDetail, self).delete(request, *args, **kwargs)
        
        
class FriendshipList(PermissionMixin, WiseListCreateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    serializer_class = WiseFriendshipSerializer
    
    
    usermodel=get_model_from_settings(settings.AUTH_USER_MODEL)
    friendshipmodel = get_model_from_settings(settings.FRIENDSHIP_MODEL)
    
    
    @property
    def owner(self):
        try:
            return self._owner
        except AttributeError:
            self._owner = get_object_or_404(self.usermodel, uri_name = self.kwargs['uri_name'])
            return self._owner
    
    def get_queryset(self):
        wiseuser = get_object_or_404(self.usermodel, uri_name = self.kwargs['uri_name'])
        friend_list = self.friendshipmodel.objects.get_friend_list(user = wiseuser)
        self.qs = friend_list
        return super(FriendshipList, self).get_queryset()
    
        
    def get(self, request, *args, **kwargs):
        """
        
        Function : Lists the friends of the user.  
        
        Permission : Authenticated user only. The user corresponding to the 
        uri_name and friends of the user are allowed access.
               
        ---
        
        omit_parameters:
            - path
            
        
        responseMessages:
            - code : 404
              message : This error occurs if the uri_name provided does not \
              correspond to a valid user on the system.
        """
        total_friends = self.friendshipmodel.objects.get_total_friends(user = self.owner)
        request_type = self.get_request_type(request = request, 
            view = self.__class__.__name__, obj = None, owner = self.owner) 
        if request_type == 'owner':
            total_mutual_friends = None
        else:    
            total_mutual_friends =  self.friendshipmodel.objects.get_total_mutual_friends(
                userA = request.user, userB = self.owner)

        response = super(FriendshipList, self).get(request, *args, **kwargs)
        response.data = {'total_friends' : total_friends, 
                        'total_mutual_friends': total_mutual_friends,
                        'friend_list' : response.data}
        return response
        
         
        
    def post(self, request, uri_name, *args, **kwargs):
        """
        
        Function : Sends a friend request to the user corresponding to uri_name 
        
        Permission : Authenticated user only. Anyone other than the user 
        corresponding to uri_name is allowed access.     
        ---
        
        omit_parameters:
            - path
            - body
            
        
        responseMessages:
            - code : 404
              message : This error occurs if the uri_name provided does not \
              correspond to a valid user on the system.
            - code : 403
              message : This error occurs if the user making the request \
              is the user corresponding to uri_name. Basically someone trying \
              to send themselves a friend request.
            - code : 409
              message : This error occurs if the user making the request \
              has already sent the person a friend request or is already \
              friends with the person
        
        
        """
        self.error_dict = { 'owner' : 'you cannot send yourself a friend request'}
        permit = self.permit(request = self.request, view = self.__class__.__name__, 
            obj = None, owner = self.owner)
        if not permit:
            error_key = self.get_request_type(request = self.request, view = self.__class__.__name__, 
            obj = None, owner = self.owner)
            raise PermissionDenied(detail = self.error_dict[error_key])
        followee = get_object_or_404(self.usermodel, uri_name = self.kwargs['uri_name'])
        follower =  self.request.user
        try:
            self.friendshipmodel.objects.create(follower = follower, followee = followee, status = 'R')
            return Response({'message' : 'your friend request has been sent'})
        except IntegrityError:
            friendship = self.friendshipmodel.objects.get(follower = follower, followee = followee)
            if friendship.status == 'F':
                return Response({'detail' : 'you are already friends with this person'}, 
                     status = status.HTTP_409_CONFLICT)
            return Response({'detail' : 'you have already sent this person a friend request'}, 
                     status = status.HTTP_409_CONFLICT) 

        
        
        
        
        
    
    
    

    
        
    
        
        
        
    
        

    