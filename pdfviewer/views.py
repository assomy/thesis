from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from models import Document
from pdfviewer.forms import DocumentForm

from django.contrib.auth.decorators import login_required
# Create your views here.
def page_png(request, document_id, page_id=None):
   if page_id == None:
      page_id = request.GET.get("page_id", 0)
      page_id = int(page_id)
      d = get_object_or_404(Document, pk=document_id)
      p = d.get_page(page_id)
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
   page = d.get_page(page_id)
   print "this is the page index.html"
   return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def index(request,page_id=None):
      all=Document.objects.order_by( '-id' )
      #all=Document.objects.order_by( '-id' )[:10] #select the first 10 books
      pictures=[]
      names=[]
      ids=[]
      for x in all:
        url=x.get_page(0).get_absolute_url()
        id=x.id
        ids.append("/"+str(id)+"p0.html")  #url format , check pdfviews.urls
        pictures.append(url)
        names.append(x.title)
      print pictures
      print names
      books=zip(pictures,ids,names)
      print books
      print list
      return render_to_response('covers.html', locals(), context_instance=RequestContext(request))
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
      return HttpResponseRedirect('/uploadsuccess')
  else:
    print "not valid document!"
    form = DocumentForm(request.POST,request.FILES)
  variables = RequestContext(request, {
    'form': form
  })
  print variables
  return render_to_response('pdf/upload.html', locals(), context_instance=RequestContext(request))
  #return render_to_response('pdf/upload.html', variables)
