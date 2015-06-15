from django.conf import settings
from django.utils.translation import ugettext_lazy as _ 

from issuewise.utils import get_model_from_settings

from rest_framework import serializers

class SocialLinkSerializer(serializers.ModelSerializer):  

    url = serializers.URLField(source = 'get_absolute_url', read_only=True,
        help_text = _('url for this social link'))
    website = serializers.CharField(source = 'get_link_type_display',
        read_only = True, help_text=_('website corresponding to this link \
        possible options are facebook, twitter, linkedin, quora, wikipedia and \
        blog'))
    privacy_description = serializers.CharField(source = 'get_privacy_display',
        read_only = True, help_text = _('a help text for understanding the current \
        privacy setting'))

    class Meta:
        social_link_model = get_model_from_settings(settings.SOCIAL_LINK_MODEL)
        model = social_link_model
        exclude = ('autobiographer','id',)
        write_only_fields = ('link_type',)