from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from models import Document
from pdfviewer.forms import DocumentForm

from django.contrib.auth.decorators import login_required
# view books by pages
def page_png(request, document_id, page_id=None):
   page_id = int(page_id)
   print "request page id",page_id
   d = get_object_or_404(Document, pk=document_id)
   if page_id>d.num_pages-1:
       page_id=d.num_pages-1
   print "serving page id",page_id
   page = d.get_page(page_id)
   title=d.title
   print "this is the page index.html"
   if  page_id>0:
       prev_page=page_id-1
       prev_page=("/"+document_id+"p"+str(prev_page)+".html")
   print "...",d.num_pages
   next_page=page_id
   next_page=("/"+document_id+"p"+str(next_page)+".html")
   if page_id < d.num_pages-1:
       print d.info
       next_page=page_id+1
       next_page=("/"+document_id+"p"+str(next_page)+".html")
   return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def index(request,page_id=None):
      all=Document.objects.order_by( '-id' )
      #all=Document.objects.order_by( '-id' )[:10] #select the first 10 books
      books=prepare_books(all)

      return render_to_response('covers.html', locals(), context_instance=RequestContext(request))
 #  return HttpResponseRedirect(p.get_absolute_url())

def prepare_books(all):
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
    return books

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





