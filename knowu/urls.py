from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # login
                       url(r'^$', 'state_scraper.views.login_user'),
                       (r'^login/$', 'state_scraper.views.login_user'),

                       # logout
                       (r'^logout/$', 'state_scraper.views.logout_user'),

                       # home
                       (r'^home/$', 'state_scraper.views.home'),

                       # geodata
                       url(r'^geodata/$', 'state_scraper.views.geodata', name='geodata'),

                       # django admin
                       url(r'^admin/', include(admin.site.urls)),
                       )
