from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context,loader,RequestContext
from django.shortcuts import render,render_to_response
from django.contrib.auth import logout as auth_logout

from social_auth import __version__ as version
# Create your views here.

def login(request):
    if request.user.is_authenticated():
  #      return HttpResponseRedirect('logout')
        return HttpResponse("aaa")
    else:
        return render_to_response('login.html', {'version': version}, RequestContext(request))


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')

def done(request):
    return HttpResponse('asd')

def loggedin(request):
    return HttpResponse('loggedin')