from django.conf.urls import url, include

from views import (Accounts, ActivationLinkCheck, ActivationLinkCreate, 
            ObtainTokenForActivatedUsers, AcceptRejectFriend, PasswordResetLinkCreate,
            Password,)                 

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
        regex = r'^friendships/(?P<pk>.+)/$',
        view = AcceptRejectFriend.as_view(),
        name = 'acceptrejectfriend',
        ),
    url(
        regex = r'^password-reset-links',
        view = PasswordResetLinkCreate.as_view(),
        name = 'password-reset-link-create',
        ),
    url(
        regex = r'^password-reset-links/(?P<uuid>.+)/$',
        view = PasswordResetLinkCheck.as_view(),
        name = 'password-reset-link-create',
        ),
    url(
        regex = r'^(?P<uri_name>.+)/password/$',
        view = Password.as_view(),
        name = 'password',
        ),
        
]