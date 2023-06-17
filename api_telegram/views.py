from django.http import Http404
from django.shortcuts import render
from .serializers import Do_S
from todo.models import Does
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import get_user
from rest_framework import generics,views, response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


class Do_API(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request,pk=None):
        
            
        try:
            token=request.headers["Authorization"][6:]
        except:
            return response.Response({"status":"error","error":"no headers"})
        if pk:
            user=Token.objects.filter(key=token)[0]
            do=Does.objects.filter(user=user.user.id, id=pk)[0]           
            ser=Do_S(do)
            return response.Response({"status":"success","data":ser.data})
        user=Token.objects.filter(key=token)[0]
        data=Does.objects.filter(user=user.user.id)
        ser=Do_S(data,many=True)
        return response.Response({"status":"success","data":ser.data})
    def post(self,request):
        ser=Do_S(data=request.data)
        try:
            ser.is_valid(raise_exception=True)
            title=ser.data.get("title")
            text=ser.data.get("text")
            token=request.headers["Authorization"][6:]
            user=Token.objects.filter(key=token)[0].user
            
            Does.objects.create(title=title,text=text,user=user)
            
        except Exception as e:
            return response.Response({"error":e.args})
        return response.Response(ser.data, status=status.HTTP_201_CREATED)
    def get_object(self, pk):
        try:
            return Does.objects.get(pk=pk)
        except Does.DoesNotExist:
            raise Http404
    def delete(self,request,pk,format=None):
        obg=self.get_object(pk)
        obg.delete()
        return response.Response({"status":"success"})
    def put(self,request,pk):
        obg=self.get_object(pk)
        ser=Do_S(obg,data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return response.Response({"status":"success","data":ser.data})





@api_view(["POST"])
def check_token(request):
    token=request.headers["Authorization"][6:]
    user=Token.objects.filter(key=token)
    if len(user)>0:
        return response.Response({"status":"success"})
    return response.Response({"status":"error","error":"wrong token"})
    