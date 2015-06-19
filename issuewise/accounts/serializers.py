from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.reverse import reverse
from rest_framework import exceptions

from accounts.models import WiseUser, WiseFriendship
from issuewise.utils import get_model_from_settings


class WiseUserSerializer(serializers.ModelSerializer):

    usermodel = get_model_from_settings(settings.AUTH_USER_MODEL)

    def create(self, validated_data):
        return self.usermodel.objects.create_user(activity_status = 'I', explanation = 'NV', **validated_data)    

    class Meta:
        model = get_model_from_settings(settings.AUTH_USER_MODEL)
        fields = ('name', 'email', 'password', 'uri_name')
        read_only_fields = ('uri_name',)
        extra_kwargs = {
            'name': {
                'error_messages' : {
                    'blank': _("Don't forget to tell us your name"),
                    'max_length': _("Your name is too long. Tell us your nickname instead. \
Make sure it is less than 200 characters long"),
                },
            },
            'email': {
                'error_messages' : {
                    'blank': _("Don't tell us you don't have an email? We can't \
believe that..."),
                    'invalid': _("That certainly doesn't look like an email id"),
                },
                'validators' : [UniqueValidator(queryset=WiseUser.objects.all(),
                    message = _("Someone has signed up already using this email \
id. If you are not that someone, maybe you should get worried."))],
            },
            'password': {
                'error_messages' : {
                    'blank': _("Don't be so trustworthy. Give your account a password"),
                },
                'write_only' : True,
                
            },
        }
       
            
  
        
        
        
class WiseFriendSerializer(serializers.ModelSerializer):
        
    profile = serializers.SerializerMethodField('get_follower_profile_url', 
        read_only = True)
        
    def get_follower_profile_url(self,obj):
        uri_name = obj.uri_name
        return reverse('accounts:userprofile:profile', 
            kwargs = {'uri_name' : uri_name}, request = self.context['request'])
        
        
    class Meta:
        model = get_model_from_settings(settings.AUTH_USER_MODEL)
        fields = ('name','profile',)
        read_only_fields = ('name',)
        
        
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password)

            if not user:
                #if not user.is_active:
                #    msg = _('User account is disabled.')
                #    raise exceptions.ValidationError(msg)
                
            #else:
                msg = _('Your email or password is incorrect')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs
        
         
                    