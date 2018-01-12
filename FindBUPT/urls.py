from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from views import home
from account.views import login_view, logout_view, register_view, createPersonalInfo_view, toPersonalManagement_view, toSharePosition_view, sharePosition_view, showSelfPosition_view, toFindPerson_view, findPerson_view, toFindPlace_view, findPlace_view, showPlacePosition_view, showPersonPosition_view, toFindNotice_view, findPublicNotice_view, showPublicNotice_view, toFindPlaceByMap_view, toFindPersonTeacher_view

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'FindBUPT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

	('^index/$', home),
    (r'^accounts/login/$', login_view),
    (r'^accounts/logout/$', logout_view),
    (r'^accounts/register/$', register_view),
    (r'^accounts/createPersonalInfo/$', createPersonalInfo_view),
    (r'^accounts/personalManage/$', toPersonalManagement_view),
    (r'^accounts/sharePosition/$', toSharePosition_view),
    (r'^accounts/sendPosition/$', sharePosition_view),
    (r'^accounts/showSelfPosition/$', showSelfPosition_view),
    (r'^accounts/toFindPerson/$', toFindPerson_view),
    (r'^accounts/FindPerson/$', findPerson_view),
    (r'^accounts/toFindPlace/$', toFindPlace_view),
    (r'^accounts/FindPlace/$', findPlace_view),
    (r'^accounts/showPlacePosition/$', showPlacePosition_view),
    (r'^accounts/showPersonPosition/$', showPersonPosition_view),
    (r'^accounts/toFindNotice/$', toFindNotice_view),
    (r'^accounts/FindNotice/$', findPublicNotice_view),
    (r'^accounts/showPublicNotice/$', showPublicNotice_view),
    (r'^accounts/toFindPlaceByMap/$', toFindPlaceByMap_view),
    (r'^accounts/toFindPersonTeacher/$', toFindPersonTeacher_view),

)

urlpatterns += staticfiles_urlpatterns()

