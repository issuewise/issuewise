from django.http import Http404
from django.shortcuts import get_object_or_404
from django.conf import settings

from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

from issuewise.utils import get_model_from_settings
from core.views import PermissionMixin, WiseListCreateAPIView, WiseRetrieveUpdateDestroyAPIView, WiseRetrieveUpdateAPIView
from core.serializers.social_link_serializers import SocialLinkSerializer
from accounts.models import WiseUser
from userprofile.models import WiseUserProfile
from userprofile.serializers import WiseUserProfileSerializer


class PersonalInfo(PermissionMixin, WiseRetrieveUpdateAPIView):

    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = WiseUserProfileSerializer
        

    # define the object by overriding get_object
    
    def get_object(self):
        
        wiseuser = get_object_or_404(WiseUser, uri_name = self.kwargs['uri_name'])
        obj = get_object_or_404(WiseUserProfile, autobiographer = wiseuser)
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
        
        return super(PersonalInfo, self).put(request, *args, **kwargs)
        
    
        
        
class SocialLinkList(PermissionMixin, WiseListCreateAPIView):
    
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = SocialLinkSerializer
    
    def get_queryset(self):
        user_model = get_model_from_settings(settings.AUTH_USER_MODEL)
        wiseuser = get_object_or_404(user_model, uri_name = self.kwargs['uri_name'])
        social_link_model = get_model_from_settings(settings.SOCIAL_LINK_MODEL)
        links = social_link_model.objects.filter(autobiographer = wiseuser)
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
        
        return super(SocialLinkList, self).post(request, *args, **kwargs) 
        
        
        

class SocialLinkDetail(PermissionMixin, WiseRetrieveUpdateDestroyAPIView):

    
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = SocialLinkSerializer
    
    def get_object(self):
        social_link_model = get_model_from_settings(settings.SOCIAL_LINK_MODEL)
        social_link = get_object_or_404(social_link_model, id = self.kwargs['pk'])
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
        
        return super(SocialLinkDetail, self).delete(request, *args, **kwargs)
        
    
    
    

    
        
    
        
        
        
    
        

    