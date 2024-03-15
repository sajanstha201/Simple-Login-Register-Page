from django.db import models

class foreign_person(models.Model):
    name=models.CharField(max_length=50,unique=True)
    year=models.IntegerField(default=0)
    credit=models.IntegerField(default=4)
    
class person(models.Model):
    name=models.CharField(max_length=50,default='')
    age=models.IntegerField(default=20)
    level=models.ForeignKey(foreign_person,to_field='name',on_delete=models.CASCADE)
    
class user_model(models.Model):
    firstname = models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    password1=models.CharField(max_length=20)
    password2=models.CharField(max_length=20)
    username=models.CharField(max_length=30,default='')
    token=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    