from django.conf.urls.defaults import *

urlpatterns = patterns('pdfviewer.views',
   url("^(?P<document_id>\d+).png$", "page_png", name="pdfviewer_page_png"),
   url("^(?P<document_id>\d+)p(?P<page_id>\d+).html$", "page_png", name="pdfviewer_page_png"),
   url(r'^$', "index",name="pdfviewer_page_png"),
   url(r'^upload/', "upload",name="upload"),



)
