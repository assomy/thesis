from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.template import Context
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from urlparse import urlparse
from datetime import datetime, timedelta
from django.core.paginator import Paginator
from bookmarks.forms import *
from bookmarks.models import *

def register_page(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      user = User.objects.create_user(
        username=form.cleaned_data['username'],
        password=form.cleaned_data['password1'],
        email=form.cleaned_data['email']
      )
      return HttpResponseRedirect('/register/success/')
  else:
    form = RegistrationForm()

  variables = RequestContext(request, {
    'form': form
  })
  return render_to_response('registration/register.html', variables)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def uploadsuccess(request):
    return render_to_response('registration/uploadsuccess.html')

def success(request):
    return render_to_response('registration/success.html')

