from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from userprofile.views import (PersonalInfo, SocialLinkList, SocialLinkDetail,
                            FriendshipList, Profile)


urlpatterns =[
    url(
        regex = r'^$',
        view = Profile.as_view(),
        name = 'profile',
        ),
    url(
        regex = r'^personal-info/$',
        view = PersonalInfo.as_view(),
        name = 'personal-info'
        ),
    url(
        regex = r'^social-links/$',
        view = SocialLinkList.as_view(),
        name = 'social-link-list',
        ),
    url(
        regex = r'^social-links/(?P<pk>.+)$',
        view = SocialLinkDetail.as_view(),
        name = 'social-link-detail',
        ),
    url(
        regex = r'^friends/$',
        view = FriendshipList.as_view(),
        name = 'friendshiplist',
        ),
]


urlpatterns = format_suffix_patterns(urlpatterns)