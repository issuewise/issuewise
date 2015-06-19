from django.conf.urls import url, include

from views import (Accounts, ActivationLinkCheck, ActivationLinkCreate, 
            ObtainTokenForActivatedUsers, AcceptRejectFriend, PasswordResetLinkCreate,
            Password, PasswordResetLinkCheck)                 

urlpatterns = [
    url(
        regex  = r'^$',
        view = Accounts.as_view(),
        name = 'accounts',
        ),
    url(
        regex = r'^activation-links/$',
        view = ActivationLinkCreate.as_view(),
        name = 'activation-link-create',
        ),
    url(
        regex = r'^activation-links/(?P<uuid>.+)/$',
        view = ActivationLinkCheck.as_view(),
        name = 'activation-link-check',
        ),
    url(
        regex = r'^tokens/$',
        view = ObtainTokenForActivatedUsers.as_view(),
        name = 'obtain-token',
        ),  
    url(
        regex = r'^friendships/(?P<pk>.+)/$',
        view = AcceptRejectFriend.as_view(),
        name = 'accept-reject-friend',
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
        regex = r'^(?P<uri_name>[^/]+)/password/$',
        view = Password.as_view(),
        name = 'password',
        ),
    url(
        r'^(?P<uri_name>[^/]+)/',
        include('userprofile.urls', namespace = 'userprofile'),
        ),
]