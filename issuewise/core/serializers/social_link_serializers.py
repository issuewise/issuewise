from django.conf import settings
from django.utils.translation import ugettext_lazy as _ 

from rest_framework import serializers
from rest_framework.reverse import reverse

from issuewise.utils import get_model_from_settings

class SocialLinkSerializer(serializers.ModelSerializer):  

    href = serializers.SerializerMethodField('get_social_link_url', read_only=True,
        help_text = _('url for this social link'))
    website = serializers.CharField(source = 'get_link_type_display',
        read_only = True, help_text=_('website corresponding to this link \
        possible options are facebook, twitter, linkedin, quora, wikipedia and \
        blog'))
    privacy_description = serializers.CharField(source = 'get_privacy_display',
        read_only = True, help_text = _('a help text for understanding the current \
        privacy setting'))
        
    def get_social_link_url(self,obj):
        uri_name = obj.autobiographer.uri_name
        pk = obj.id
        return reverse('accounts:userprofile:social-link-detail', 
            kwargs = {'uri_name' : uri_name, 'pk' : pk}, request = self.context['request'])
        

    class Meta:
        social_link_model = get_model_from_settings(settings.SOCIAL_LINK_MODEL)
        model = social_link_model
        exclude = ('autobiographer','id',)
        write_only_fields = ('link_type',)