from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

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
       
            
  
        
        
        
class WiseFriendshipSerializer(serializers.ModelSerializer):

    name = serializers.PrimaryKeyRelatedField(source = 'follower.name', 
        read_only=True, help_text = _('This is one of the users \
        in the friendship relation. If the status of the friendship is R \
        (request sent), this field indicates the person who sent the request'))
        
    profile = serializers.URLField(source = 'get_follower_profile_url', 
        read_only = True)
    class Meta:
        model = get_model_from_settings(settings.FRIENDSHIP_MODEL)
        exclude = ('follower', 'followee','status','followed_at')
        
         
                    