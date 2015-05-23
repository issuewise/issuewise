from rest_framework import serializers

from userprofile.models import WiseUserProfile


class WiseUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WiseUserProfile
        exclude = ('autobiographer',)

