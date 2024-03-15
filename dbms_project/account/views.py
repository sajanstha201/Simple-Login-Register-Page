from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as login_user,logout as logout_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
def register(request):
    if(request.method=='POST'):
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if(User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            messages.error(request,'User or Email already exist')
            return redirect(reverse('register_url'))
        User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password1)
        return redirect(reverse('login_url'))
    return render(request,'account/register.html')


def login(request):
    if(request.method=='POST'):
        form=AuthenticationForm(data=request.POST)
        if(form.is_valid()):
            user=form.get_user()
            login_user(request,user)
            messages.info(request,"Login successfully")
            return redirect(reverse('home_url'))
        messages.info(request,"Invalid username or password")
    return render(request,'account/login.html')


def logout(request):
    logout_user(request)
    return redirect(reverse('login_url'))


