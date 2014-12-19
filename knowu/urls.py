from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # login
                       url(r'^$', 'state_scraper.views.login_user'),
                       url(r'^login/$', 'state_scraper.views.login_user', name='login'),

                       # logout
                       url(r'^logout/$', 'state_scraper.views.logout_user', name='logout'),

                       # home
                       url(r'^home/$', 'state_scraper.views.home', name='home'),

                       # geodata
                       url(r'^geodata/$', 'state_scraper.views.geodata', name='geodata'),

                       # django admin
                       url(r'^admin/', include(admin.site.urls)),
                       )
