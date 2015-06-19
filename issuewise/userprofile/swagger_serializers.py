from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from accounts.serializers import WiseFriendSerializer


class FriendListDisplaySerializer(serializers.Serializer):
    total_friends = serializers.IntegerField(help_text = _('total number of friends \
of the user'))
    total_mutual_friends = serializers.IntegerField(help_text = _('total number of mutual friends \
between the user and the user making the request. Returns null when both are the same.'),
        required = False)
    friend_list = WiseFriendSerializer(many = True, help_text= _('list of friends of this \
user. The friends listed here can depend on whether the requesting user is a friend of \
this user or not. If the requesting user is not a friend, only mutually friedns are returned'))
    