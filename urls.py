from django.conf.urls.defaults import *
from bookmarks.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import os
CURRENT_PATH = os.path.abspath( os.path.dirname( __file__ ).decode( 'utf-8' ) ).replace( '\\', '/' )

urlpatterns = patterns('',
    # Example:
    # (r'^example/', include('example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^', include("pdfviewer.urls")),
    (r'^register/$', register_page),

    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^register/success/$', success),
    (r'^uploadsuccess/$', uploadsuccess),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root' : os.path.join( CURRENT_PATH, 'static' ) }),
)
