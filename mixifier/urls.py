from django.conf.urls import patterns, include, url
from os import path

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

mixdir = path.abspath('./mixifier/media')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mixifier.views.home', name='home'),
    # url(r'^mixifier/', include('mixifier.foo.urls')),
    
    url(r'^$', 'mixifier.views.pick'),
    url(r'^analyze/(?P<taskid>.*)/(?P<outf>.*)/$', 'mixifier.views.analyze'),
    url(r'^mix/(?P<taskid>.*)/(?P<outf>.*)/$', 'mixifier.views.mix'),
    url(r'^play/(?P<outf>.*)/$', 'mixifier.views.play'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':mixdir,
         'show_indexes': True}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
