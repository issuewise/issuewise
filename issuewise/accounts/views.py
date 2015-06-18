from django.shortcuts import get_object_or_404
from django.conf import settings

from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import renderers

from core.views import PermissionMixin, WiseListCreateAPIView
from accounts.models import WiseUser, WiseActivation, WiseFriendship
from accounts.serializers import WiseUserSerializer, WiseFriendshipSerializer
from accounts.exceptions import UserNotActive
from issuewise.utils import get_model_from_settings


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

    def get(self, request, uuid, format = None):
        """
        
        Function : Activates the user associated with this resource. 
        
        Permission : Anonymous. Everyone is allowed access
        
        ---
        
        omit_parameters:
            - path
        
        """ 
        obj = get_object_or_404(WiseActivation, uuid = uuid)
        user = obj.creator
        user.activate()
        token, created = Token.objects.get_or_create(user=user)
        uri_name = user.uri_name
        return Response({'token': token.key, 'uri_name' : uri_name})
        
        
class PasswordResetLinkCreate(APIView):

    usermodel = get_model_from_settings(settings.AUTH_USER_MODEL)

    def post(self, request, *args, **kwargs):
        email = request.data['email']
        user = self.usermodel.objects.get(email = email)
        user.send_password_reset_email()    
        return Response({'message' : 'the password reset link was sent to your email'})
        
        
class PasswordResetLinkCheck(APIView):

    def get(self, request, uuid, *args, **kwargs):
    
        password_reset_link_model = settings.PASSWORD_RESET_LINK_MODEL

        obj = get_object_or_404(password_reset_link_model, uuid = uuid)
        user = obj.creator
        uri_name = user.uri_name
        token, created = Token.objects.get_or_create(user=user)
        obj.delete()
        return Response({
                        'token': token.key, 
                        'link' : reverse('accounts:password',
                            kwargs = {'uri_name' : uri_name}), 
                        'method' : 'post',
                        }
                        )
    
        
    
class Password(APIView):

    authentication_classes = (TokenAuthentication,)
    usermodel = get_model_from_settings(settings.AUTH_USER_MODEL)

    def post(self, request, *args, **kwargs):
        requesting_user = request.user
        owner = self.usermodel.objects.get(uri_name = self.kwargs['uri_name'])
        if requesting_user == owner:
            password = request.data['password']
            owner.set_password(password)
            owner.save()
            return Response({'message' : 'password was successfully changed'})
        else:
            raise PermissionDenied(detail="you are trying to change someone else's password")
            
            
        
        
    

        
    
    

    

    
        
        
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
            
        type:
            token:
                required: true
                type: string
                description: token used for http Token Authentication
            uri_name:
                required: true
                type: string
                description: uri friendly name of the user. all nodes with \
                {uri_node} needs to include this string in place of {uri_name}.
            
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
        type:
            token:
                required: true
                type: string
                description: token used for http Token Authentication
            uri_name:
                required: true
                type: string
                description: uri friendly name of the user. all nodes with \
                {uri_node} needs to include this string in place of {uri_name}.
              
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
        uri_name = user.uri_name
        return Response({'token': token.key, 'uri_name' : uri_name})
        
        
        
        
class AcceptRejectFriend(PermissionMixin, APIView):

    
    permission_classes = (IsAuthenticated,)
    
    
    
    def get_object(self):
        obj = get_object_or_404(WiseFriendship, id = self.kwargs['pk'])
        return obj
        
    @property    
    def owner(self):
        try:
            return self._owner
        except AttributeError:
            obj = get_object_or_404(WiseFriendship, id = self.kwargs['pk'])
            self._owner = obj.followee
            return self._owner
     
    def check_permission(self, obj):
        permit = self.permit(request = self.request, view = self.__class__.__name__,
            obj = obj, owner = self.owner)
        if not permit:
            error_key = self.get_request_type(request = self.request, view = self.__class__.__name__, 
                obj = obj, owner = self.owner)
            raise PermissionDenied(detail = self.error_dict[error_key])
    
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
        self.error_dict = {'friend' : 'you cannot accept a friend request for \
someone else' , 'stranger' : 'you cannot accept a friend request for someone else'} 
        obj = self.get_object()
        self.check_permission(obj)
        if obj.status == 'R':
            obj.status = 'F'
            obj.save()
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
        self.error_dict = {'friend' : 'you cannot delete a friend request for \
someone else' , 'stranger' : 'you cannot delete a friend request for someone else'} 
        obj = self.get_object()
        self.check_permission(obj)
        if obj.status == 'F':
            obj.delete()
            WiseFriendship.objects.get(follower = obj.followee, followee = obj.follower).delete() 
        else:
            obj.delete()
        return Response()
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
    