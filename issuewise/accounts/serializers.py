from rest_framework import serializers

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
        }
        
        
class WiseFriendshipSerializer(serializers.ModelSerializer):

    follower = serializers.PrimaryKeyRelatedField(source = 'follower.name', read_only=True)   
    followee = serializers. PrimaryKeyRelatedField(source = 'followee.name', read_only=True)
    
    class Meta:
        model = WiseFriendship
        read_only_fields = ('status',)
        extra_kwargs = {
            'follower': {
                'write_only': True,
            },
        }
                    