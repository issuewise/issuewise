from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from userprofile.views import (PersonalInfo, SocialLinkList, SocialLinkDetail,
                            FriendshipList, Profile)


urlpatterns =[
    url(
        regex = r'^profile/$',
        view = Profile.as_view(),
        name = 'profile',
        ),
    url(
        regex = r'^profile/personal-info/$',
        view = PersonalInfo.as_view(),
        name = 'personal-info'
        ),
    url(
        regex = r'^profile/social-links/$',
        view = SocialLinkList.as_view(),
        name = 'social-link-list',
        ),
    url(
        regex = r'^profile/social-links/(?P<pk>.+)$',
        view = SocialLinkDetail.as_view(),
        name = 'social-link-detail',
        ),
    url(
        regex = r'^profile/friends/$',
        view = FriendshipList.as_view(),
        name = 'friendship-list',
        ),
]


urlpatterns = format_suffix_patterns(urlpatterns)