from django.conf import settings

from issuewise.utils import get_model_from_settings

from rest_framework import serializers

class SocialLinkSerializer(serializers.ModelSerializer):  

    class Meta:
        social_link_model = get_model_from_settings(settings.SOCIAL_LINK_MODEL)
        model = social_link_model
        read_only_fields = ('website', 'autobiographer', )