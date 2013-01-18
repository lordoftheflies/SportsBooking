from django.conf.urls import patterns, include, url
from booking import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SportsBooking.views.home', name='home'),
    # url(r'^SportsBooking/', include('SportsBooking.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', views.login, name='login'),
    url(r'', include('social_auth.urls')),
    url(r'^done/$', views.done, name='done'),
    url(r'^logged-in/$',views.loggedin, name='loggedin'),
    url(r'^logout/$',views.logout, name='logout'),
    # url(r'^admin/', include(admin.site.urls)),
)
