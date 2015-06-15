from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from userprofile.models import WiseUserProfile


class WiseUserProfileSerializer(serializers.ModelSerializer):
    username = serializers.PrimaryKeyRelatedField(source = 'autobiographer.name', 
        read_only=True, help_text = _('name of the user making the request'))
    age = serializers.IntegerField(source='calculate_age', read_only=True,
        help_text = _('current age of the user'))
    privacy_description = serializers.CharField(source = 'get_privacy_display',
        read_only = True, help_text = _('a help text for understanding the current \
        privacy setting'))
    url = serializers.URLField(source = 'get_absolute_url', read_only=True,
        help_text = _('url for this node'))
    edit_method = serializers.SerializerMethodField('edit_method_func', read_only = True,
        help_text = _('in order to edit the information provided by this node \
        use this http method'))
    
    def edit_method_func(self,obj):
        return 'PUT'

    class Meta:
        model = WiseUserProfile
        exclude = ('id', 'autobiographer',)