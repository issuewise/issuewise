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
    
    def post(self, request, *args, **kwargs):
        """
        Function : Creates a new user. 
        
        Permission : Anonymous. Everyone is allowed access. 
        
        ---
        
        responseMessages:
            - code: 400
              message: This error occurs if either the username exceeds \
              200 characters or the email id is not unique or both. \
              Check the json response to find out which one of them happened.
        
        """
        return super(Accounts, self).post(request, *args, **kwargs)
    
    
class ActivationLinkCheck(APIView):

    def get(self, request, uuid, uri_name, format = None):
        """
        
        Function : Activates the user associated with this resource. 
        
        Permission : Anonymous. Everyone is allowed access
        
        ---
        
        omit_parameters:
            - path
        
        """ 
        obj = get_object_or_404(WiseActivation, uuid = uuid)
        obj.creator.activate()
        return Response() 
        
        
class ActivationLinkCreate(APIView):
    
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format = None):
        """
        Function : Performs the following activities 
        
            1. Creates an activation link
            
            2. Associates the authenticated user with the activation link 
            
            3. Sends an email to the email id of the authenticated user. This
            email contains the activation link.  
        
        Permission : Authenticated user only.IMPORTANT NOTE : This is the only 
        node where authentication is performed via Basic Http Authentication and 
        NOT Token Authentication.
        
        ---
        
        omit_parameters:
            - path
            
        responseMessages:
            - code: 403
              message: This error occurs if an user tries to activate \
              someone else's account. 
              
            - code: 401
              message : This error occurs if the request cannot be authenticated. \
              This usually means that the username and password supplied in \
              the header is wrong or the client is using a protocol different \
              from Http Basic Authentication to access this node. 
        
        """ 
        user = request.user
        #if not self.permit(self.request, self.__class__.__name__, None , user, self.kwargs):
        #    raise PermissionDenied
        user.send_activation_email()
        return Response()
        
        
class ObtainTokenForActivatedUsers(ObtainAuthToken):

    def post(self, request):
        """
        Function : Obtain the token for an user (for Token authentication)
        Permission: Anonymous. Anyone can access. Must be performed over 
        https because post data contains sensitive information.
        
        ---
        
        parameters:
            - name: username
              description: email id of the user
              required: true
              type: email
              paramType: form
            - name: password
              description : password of the user
              required : true
              type : string
              paramType: form
              
        responseMessages:
            - code : 400
              message: This error indicates authentication failure. This means \
              that the login credentials are invalid.
            - code : 403
              message: This error indicates that the authentication was \
              succesful but there is a problem with the user's account. \
              Therefore the token could not be returned. Explanation of the \
              problem can be found in the json returned.
              
        """
        
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
        
        return super(FriendshipList, self).get(request, *args, **kwargs) 
        
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
              
        
        
        """
    
        wiseuser = get_object_or_404(WiseUser, uri_name = uri_name)
        permit = self.permit(self.request, self.__class__.__name__,
            None, wiseuser, self.kwargs)
        if not permit:
            raise PermissionDenied(detail = 'you cannot send yourself a \
                friend request')
        
     
        
        return super(FriendshipList, self).post(request, uri_name, *args, **kwargs) 
        
        
        
    
        
        
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
    
        """
        
        Function : Accept the friend request corresponding to pk. 
        
        Permission : Authenticated user only. Only the  user 
        corresponding to uri_name is allowed access.     
        ---
        
        omit_parameters:
            - path
            
        
        responseMessages:
            - code : 404
              message : This error occurs if the uri_name provided does not \
              correspond to a valid user on the system or if the user \
              corresponding to uri_name does not have a friend request \
              corresponding to pk.
            - code : 403
              message : This error occurs if the user making the request \
              is not the user corresponding to uri_name. 
              
        
        
        """
        obj = self.get_object()
        self.check_permission(obj)
        if obj.status == 'R':
            obj.status = 'F'
            WiseFriendship.objects.create(follower = obj.followee, followee = obj.follower, status ='F')
        return Response()
        
    def delete(self, request, format = None, *args, **kwargs):
    
        """
        
        Function : Reject the friend request corresponding to pk or delete the
        friendship relation (unfriend) defined in the entry corresponding to pk.
        
        Permission : Authenticated user only. Only the  user 
        corresponding to uri_name is allowed access.     
        ---
        
        omit_parameters:
            - path
            
        
        responseMessages:
            - code : 404
              message : This error occurs if the uri_name provided does not \
              correspond to a valid user on the system or if the user \
              corresponding to uri_name does not have a friend request \
              corresponding to pk.
            - code : 403
              message : This error occurs if the user making the request \
              is not the user corresponding to uri_name. 
              
        
        
        """    
        obj = self.get_object()
        self.check_permission(obj)
        if obj.status == 'F':
            obj.delete()
            WiseFriendship.objects.get(follower = obj.followee, followee = obj.follower).delete()
        obj.delete()
        return Response()
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
    