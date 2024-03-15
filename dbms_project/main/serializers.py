from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import person,user_model,foreign_person
from django.contrib.auth.hashers import make_password
import secrets
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class foreign_serailizers(serializers.ModelSerializer):
    class Meta:
        model=foreign_person
        fields=['name']
        
class person_serializers(serializers.ModelSerializer):
    level=foreign_serailizers()
    history=serializers.SerializerMethodField()
    class Meta:
        model=person
        fields='__all__'
        depth=1
    def validate(self,obj):
        if(person.objects.all().filter(name=obj['name']).exists()):
            raise ValidationError("already exist")
        if(obj['age']>20):
            raise ValidationError("age cross")
        return obj
    def get_history(self,obj):
        return "MIT"
    
    
class register_serializers(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    def validate(self,obj):
        if(User.objects.all().filter(username=obj['username'])):
            raise ValidationError("user aldready exist")      
        return obj
    def create(self,obj):
        instance=User(**obj)
        instance.set_password(obj['password'])
        instance.save()
        return instance
    
class login_serializers(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()