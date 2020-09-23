from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.defaults import page_not_found
# from weasyprint import HTML
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes

from rest_framework import status,viewsets
from rest_framework.response import Response
import os, hashlib, warnings, requests, json


from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny

from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view,renderer_classes

from rest_framework import permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.parsers import FormParser,MultiPartParser
from rest_framework.decorators import parser_classes
# Create your views here.
def home(request):
    return HttpResponse('welcome to SPENN apis gateway')

class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
             
        serializer = UserSerializerWithToken(data = request.data)
        if serializer.is_valid():
            saved_user = serializer.save()
        else:
            return Response({"response" : "error", "message" : serializer.errors})
        return Response({"response" : "success", "message" : "Succesfull"})

@api_view(['GET'])
def get_current_user(request):
    serializer = GetFullUserSerializer(request.user)
    return Response(serializer.data,status=status.HTTP_200_OK)

# Money sending serializers
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([])
def moneysendapi(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        snippets = Moneysend.objects.filter(agent=request.user).order_by('-id')[:10]
        serializer = MoneSendSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MoneSendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(APIView):
    def get(self,request):
        snippets =  Moneysend.objects.filter().order_by('-id')[:20]
        serializer =  MoneSendSerializer(snippets, many=True)
        return JsonResponse(serializer.data)

    # return JsonResponse(serializer.data, safe=False)