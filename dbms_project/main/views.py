from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import person,user_model,foreign_person
from .serializers import person_serializers,login_serializers,register_serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
@login_required
def home(request):
    return render(request,'home.html')

@api_view(['POST'])
def post(request):
    data=request.data
    obj=person(**data)
    obj.save()
    return Response({"status":"success"})

@api_view(['GET','POST','PATCH'])
def file(request):
    if(request.method=='POST'):
        data=request.data
        obj=person(name=data['name'],age=data['age'],level=data['level'])
        ser=person_serializers(data=person_serializers(obj).data)
        if ser.is_valid():
            obj.save()
            return Response({"status":"success"})
        else:
            print(ser.errors)
            return Response(ser.errors)
    elif(request.method=='GET'):
        all_obj=person.objects.all()
        obj_dict=person_serializers(all_obj,many=True)
        return Response(obj_dict.data)
    else:
        return Response({"name":"kathmandu"})
        
        
@api_view(['POST','GET'])
def login_function(request):
    if(request.method=='POST'):
        login_ser=login_serializers(data=request.data)
        obj=user_model(**request.data)
        if(login_ser.is_valid()):
            obj.save()
            return Response({"status":"success"})
    if(request.method=='GET'):
        return Response({"status":"GET"})
    return Response({"status":"fail"})
    
    
    
    
class register_api(APIView):
    def post(self,request):
        ser=register_serializers(data=request.data)
        if(ser.is_valid()):
            ser.create(ser.data)
            return Response({"status":"reigstered the user"})
        else:
            return Response(ser.errors)
            
class login_api(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        ser=login_serializers(data=request.data)
        if not ser.is_valid():
            return Response({"status":"invalid data"})
        usr=authenticate(username=ser.validated_data['username'],password=ser.validated_data['password'])
        if not usr:
            return Response({"status":"invalid username or password"})
        token,created=Token.objects.get_or_create(user=usr)
        return Response({"status":"login success","token":str(token)})

class tweets(APIView):
    def get(self,request):
        return Response({"status":"get"})
    def post(self,request):
        data=request.data
        
        return Response({"status":"post"})
    def pust(self,request):
        return Response({"status":"put"})