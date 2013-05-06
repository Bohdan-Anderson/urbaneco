from django.conf.urls import patterns, include, url
from django.conf.urls import patterns, url

from urbaneco.views import EventListView, EventDetailView
from urbaneco.views import SpeakerListView, SpeakerDetailView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'urbaneco.views.home', name='home'),
    
    #url(r'^events/', 'urbaneco.views.event_list', name='events'),
    url(r'^speakers/(?P<slug>[-_\w]+)/$', SpeakerDetailView.as_view(), name='speaker-detail'),
    # url(r'^urbaneco/', include('urbaneco.foo.urls')),
    url(r'^events/(?P<slug>[-_\w]+)/$', EventDetailView.as_view(), name='event-detail'),
    
    
    url(r'^events/', EventListView.as_view(), name='event-list'),
    url(r'^speakers/', SpeakerListView.as_view(), name='speaker-list'),
       
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
