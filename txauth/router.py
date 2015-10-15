from django.http import Http404, HttpResponseNotAllowed  
from django.conf.urls import url  
  
GET = 'GET'  
PUT = 'PUT'  
POST = 'POST'  
HEAD = 'HEAD'  
TRACE = 'TRACE'  
DELETE = 'DELETE'  
OPTIONS = 'OPTIONS'  
  
HTTP_METHODS = (GET, POST, PUT, HEAD, DELETE, OPTIONS, TRACE)  
  
def dispatch(request, *args, **kwargs):  
    view = kwargs.pop(request.method, None)  
    if view:  
        for method in HTTP_METHODS:  
            kwargs.pop(method, None)  
        return view(request, *args, **kwargs)  
    else:  
        allowed_methods = []  
        for method in HTTP_METHODS:  
            if kwargs.pop(method, None):  
                allowed_methods.append(method)  
        if allowed_methods:  
            return HttpResponseNotAllowed(allowed_methods)  
        else:  
            raise Http404  
  
def mapping(regex, viewname, get = None, post = None, put = None, delete = None, head = None, options = None, trace = None):  
    views = { GET: get, POST: post, PUT: put, DELETE: delete, HEAD: head,OPTIONS: options, TRACE: trace }  
    return url(regex, dispatch, views, viewname)