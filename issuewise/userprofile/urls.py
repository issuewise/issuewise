from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from userprofile.views import PersonalInfo, SocialLinkList, SocialLinkDetail


urlpatterns =[
    url(
        regex = r'^personal-info/$',
        view = PersonalInfo.as_view(),
        name = 'personal_info'
        ),
    url(
        regex = r'^social-links/$',
        view = SocialLinkList.as_view(),
        name = 'social_link_list',
        ),
    url(
        regex = r'^social-links/(?P<pk>.+)$',
        view = SocialLinkDetail.as_view(),
        name = 'social_link_detail',
        )
    
]


urlpatterns = format_suffix_patterns(urlpatterns)