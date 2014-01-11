from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from models import Document
from pdfviewer.forms import *

from django.contrib.auth.decorators import login_required
# Create your views here.
def page_png(request, document_id, page_id=None):
   if page_id == None:
      page_id = request.GET.get("page_id", 0)
      page_id = int(page_id)
      d = get_object_or_404(Document, pk=document_id)
      p = d.get_page(page_id)
      pictures_page=p
      all=Document.objects.all()
      pictures=[]
      for x in all:
        url= x.get_page(0).get_absolute_url()
        pictures.append(url)
      print pictures
      print "this page png "
      return render_to_response('covers.html', {"pictures": pictures},context_instance=RequestContext(request))
   page_id = int(page_id)
   d = get_object_or_404(Document, pk=document_id)
   p = d.get_page(page_id)
   pictures_page=p
   print dir(p)
   return render_to_response('index.html', {"pictures_page": pictures_page},context_instance=RequestContext(request))
def index(request,page_id=None):
      all=Document.objects.all()
      pictures=[]
      names=[]
      for x in all:
        url=x.get_page(0).get_absolute_url()
        pictures.append(url)
        names.append(x.title)
      print pictures
      print names
      books=zip(pictures,names)
      print list
      return render_to_response('covers.html', {"pictures": pictures,"books":books},context_instance=RequestContext(request))
 #  return HttpResponseRedirect(p.get_absolute_url())

@login_required
def upload(request):
  if request.method == 'POST':
    print request.POST
    form = DocumentForm(request.POST, request.FILES)
    print "found Post!"
    if form.is_valid():
      Doc=form.save(commit=False)
      Doc.save()
      return HttpResponseRedirect('/register/success/')
  else:
    print "not valid document!"
    form = DocumentForm(request.POST,request.FILES)
  variables = RequestContext(request, {
    'form': form
  })
  return render_to_response('pdf/upload.html', variables)
