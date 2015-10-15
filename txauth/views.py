# -*- coding: utf-8 -*-
#from atom.http_core import HttpResponse
true=True
false=False
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework import views, status
from rest_framework.decorators import api_view
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.template import RequestContext
from StringIO import StringIO
from zipfile import ZipFile
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo import mongo_client
from django.views.generic import TemplateView
from uuid import uuid4
import urllib, datetime
connection = MongoClient(settings.DATABASES["default"]["HOST"], port=27017)
db=connection[settings.DATABASES["default"]["NAME"]]
context = "copyright @ 2015, Atul Jain you can contribute as opensource application "
@api_view(['GET'])
def MAIN(request):
    if request.method == 'GET':
        return render_to_response('login.html',context)
    return Response(status=501)

@api_view(['GET'])
def home(request):
    return render_to_response('home.html', {"context":context, "Mesage":"This is the demo Home Page "})

@api_view(['POST'])
def login_a(request):
    username = request.POST.get('username')
    password = request.POST.get('passsword')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            request.session["username"]=user.username
            request.session["is_authorized"]=True
            request.session["is_superuser"]=user.is_superuser
            request.session["is_staff"]=user.is_staff
            # response = HttpResponseRedirect('/home/?redirect_to='+str(redirect_to), {
            #     "username":request.session["username"]
            # })
            # return response
            return HttpResponseRedirect('/home')
        else:
            return render_to_response('login.html', context)
    else:
        return render_to_response('login.html', context)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#https://netbeam.baxterthompson.com/