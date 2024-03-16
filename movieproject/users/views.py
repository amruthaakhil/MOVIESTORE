from django.contrib import messages, auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import  UpdateProfileForm

from .models import Profile


# Create your views here.
@login_required
def view_profile(request):
    profile = request.user.profile
    return render(request, 'view_profile.html', {'profile': profile})

def edit_profile(request):
    if request.method == 'POST':
        form=UpdateProfileForm(request.POST,instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Profile is updated successfully')
            return redirect('view_profile/')
    else:
        form = UpdateProfileForm(instance=request.user.profile)
        messages.error(request,'Error updating you profile')
    return render(request,"profile.html",{'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"WELCOME")
            return redirect ('/')
        else:
            messages.info(request,"Invalid user")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        bio = request.POST['bio']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Exist!")
                return redirect('users:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email id already exist.")
                return redirect('users:register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                return redirect('users:login')
        else:
            messages.info(request, "Password not matching")
            return redirect('users:register')
        return redirect('/')


    return render(request,"register.html")