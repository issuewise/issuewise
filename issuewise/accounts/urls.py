from django.conf.urls import url, include

from views import (Accounts, ActivationLinkCheck, ActivationLinkCreate, 
            ObtainTokenForActivatedUsers, FriendshipList, AcceptRejectFriend)                 

urlpatterns = [
    url(
        regex  = r'^$',
        view = Accounts.as_view(),
        name = 'accounts',
        ),
    url(
        regex = r'^activation-links/$',
        view = ActivationLinkCreate.as_view(),
        name = 'activationlinkcreate',
        ),
    url(
        regex = r'^activation-links/(?P<uuid>.+)/$',
        view = ActivationLinkCheck.as_view(),
        name = 'activationlinkcheck',
        ),
    url(
        regex = r'^tokens/$',
        view = ObtainTokenForActivatedUsers.as_view(),
        name = 'obtaintoken',
        ),  
    url(
        regex = r'^(?P<uri_name>.+)/friendships/$',
        view = FriendshipList.as_view(),
        name = 'friendshiplist',
        ),
    url(
        regex = r'^(?P<uri_name>.+)/friendships/(?P<pk>.+)/$',
        view = AcceptRejectFriend.as_view(),
        name = 'acceptrejectfriend',
        ),
]