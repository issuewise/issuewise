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
        
        

class SocialLinkDetail(PermissionMixin, WiseRetrieveUpdateDestroyAPIView):

    
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = SocialLinkSerializer
    
    def get_object(self):
        social_link_model = get_model_from_settings(settings.SOCIAL_LINK_MODEL)
        social_link = get_object_or_404(social_link_model, id = self.kwargs['pk'])
        self.obj = social_link
        return super(SocialLinkDetail, self).get_object()  
    
    
    
    
    
    

    
        
    
        
        
        
    
        

    