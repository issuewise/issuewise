from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from core.views import Welcome 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'issuewise.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(
        r'^admin/', 
        include(admin.site.urls),
        ),
    url(
        r'^docs',
        include('rest_framework_swagger.urls', namespace = 'documentation')
        ),
    url(
        regex = r'^$',
        view = Welcome.as_view(),
        name = 'welcome',
        ),
    url(
        r'^', 
        include('rest_framework.urls', namespace = 'rest_framework'),
       ),
    url(
        r'^users/(?P<uri_name>.+)/profile/', 
        include('userprofile.urls', namespace = 'userprofile'),
        ), 
    url(
        r'^users/', 
        include('accounts.urls', namespace = 'accounts'),
        ),
)