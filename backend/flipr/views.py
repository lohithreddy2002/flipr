from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import  api_view, permission_classes,authentication_classes
from rest_framework.response import  Response
from django.contrib.auth.models import User,auth
from .seri import TitleSerializer
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
import json
# Create your views here.
@api_view(['GET'])
def home(request):
    print(request.user)
    return Response({"a"})

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = auth.authenticate(username = email,password = password)
    if user is not None:
        login(request,user)
    else:
        print("bye")
        
    return Response("sucess")

@permission_classes((AllowAny,))
@api_view(['POST','GET'])
def register(request):
    if(request.method == "GET"):
        print(request.user)
        return Response("sucess")
    else:
        print(request.data)
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.create(username = email,email=email, password=password)        
        return Response('sucess')



