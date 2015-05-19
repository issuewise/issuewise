from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from core.views import PermissionMixin, WiseListCreateAPIView
from accounts.models import WiseUser, WiseActivation, WiseFriendship
from serializers import WiseUserSerializer, WiseFriendshipSerializer
from exceptions import UserNotActive


class Accounts(generics.CreateAPIView):

    model = WiseUser
    serializer_class = WiseUserSerializer
    
    
    
class ActivationLinkCheck(PermissionMixin, APIView):

    def get(self, request, uuid, uri_name, format = None):
        obj = get_object_or_404(WiseActivation, uuid = uuid)
        obj.creator.activate()
        return Response() 
        
        
class ActivationLinkCreate(PermissionMixin, APIView):
    
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request,uri_name, format = None):
        user = get_object_or_404(WiseUser, uri_name = uri_name)
        if not self.permit(self.request, self.__class__.__name__, None , user, self.kwargs):
            raise PermissionDenied
        user.send_activation_email()
        return Response()
        
        
class ObtainTokenForActivatedUsers(ObtainAuthToken):

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user.activity_status == 'I':
            raise UserNotActive(explanation = user.explanation)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
        
        
class FriendshipList(PermissionMixin, WiseListCreateAPIView):

    permission_classes = (IsAuthenticated,)
    
    serializer_class = WiseFriendshipSerializer
    
    def get_queryset(self):
        wiseuser = get_object_or_404(WiseUser, uri_name = self.kwargs['uri_name'])
        friend_list = WiseFriendship.objects.filter(follower = wiseuser, status = 'F')
        self.qs = friend_list
        return super(FriendshipList, self).get_queryset()
    
    def perform_create(self, serializer):
        followee = get_object_or_404(WiseUser, uri_name = self.kwargs['uri_name'])
        follower = self.request.user
        serializer.save(follower = follower, followee = followee, status = 'R')
        
        
class AcceptRejectFriend(PermissionMixin, APIView):

    
    permission_classes = (IsAuthenticated,)
    
    def get_object(self):
        obj = get_object_or_404(WiseFriendship, id = self.kwargs['pk'])
        return obj
     
    def check_permission(self, obj):
        permit = self.permit(self.request, self.__class__.__name__,
            None, obj, self.kwargs)
        if not permit:
            raise PermissionDenied
    
    def put(self, request, format = None, *args, **kwargs):
        obj = self.get_object()
        self.check_permission(obj)
        if obj.status == 'R':
            obj.status = 'F'
            WiseFriendship.objects.create(follower = obj.followee, followee = obj.follower, status ='F')
        return Response()
        
    def delete(self, request, format = None, *args, **kwargs):
        obj = self.get_object()
        self.check_permission(obj)
        if obj.status == 'F':
            obj.delete()
            WiseFriendship.objects.get(follower = obj.followee, followee = obj.follower).delete()
        obj.delete()
        return Response()
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
    