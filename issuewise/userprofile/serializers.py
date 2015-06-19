from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from rest_framework import serializers
from rest_framework.reverse import reverse

from issuewise.utils import get_model_from_settings


class WiseUserProfileSerializer(serializers.ModelSerializer):
    username = serializers.PrimaryKeyRelatedField(source = 'autobiographer.name', 
        read_only=True, help_text = _('name of the user making the request'))
    age = serializers.IntegerField(source='calculate_age', read_only=True,
        help_text = _('current age of the user'))
    privacy_description = serializers.CharField(source = 'get_privacy_display',
        read_only = True, help_text = _('a help text for understanding the current \
        privacy setting'))
    href = serializers.SerializerMethodField('get_personal_info_url', read_only=True,
        help_text = _('url for this node'))
    edit_method = serializers.SerializerMethodField('edit_method_func', read_only = True,
        help_text = _('in order to edit the information provided by this node \
        use this http method'))
        
        
    def get_personal_info_url(self,obj):
        uri_name = obj.autobiographer.uri_name
        return reverse('accounts:userprofile:personal-info', 
            kwargs = {'uri_name' : uri_name}, request = self.context['request'])
    
    def edit_method_func(self,obj):
        return 'PUT'

    class Meta:
        model = get_model_from_settings(settings.USER_PROFILE_MODEL)
        exclude = ('id', 'autobiographer',)