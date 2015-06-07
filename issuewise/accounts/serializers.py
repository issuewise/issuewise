from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from accounts.models import WiseUser, WiseFriendship


class WiseUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return WiseUser.objects.create_user(activity_status = 'I', explanation = 'NV', **validated_data)    

    class Meta:
        model = WiseUser
        fields = ('name', 'email', 'password', 'uri_name')
        read_only_fields = ('uri_name',)
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
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
            },
        }
       
            
  
        
        
        
class WiseFriendshipSerializer(serializers.ModelSerializer):

    follower = serializers.PrimaryKeyRelatedField(source = 'follower.name', 
        read_only=True, help_text = _('This is one of the users \
        in the friendship relation. If the status of the friendship is R \
        (request sent), this field indicates the person who sent the request'))   
    followee = serializers. PrimaryKeyRelatedField(source = 'followee.name', 
        read_only=True, help_text = _('This is one of the users \
        in the friendship relation. If the status of the friendship is R \
        (request sent), this field indicates the person who received the request'))
    
    class Meta:
        model = WiseFriendship
        read_only_fields = ('status',)
        extra_kwargs = {
            'follower': {
                'write_only': True,
            },
        }
                    