from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseForbidden

from .models import UserDetail
from .forms import SignUpForm,UserDetailForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})    

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('displayprofile')  # Redirect to profile page after login
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    try:
        user_detail = UserDetail.objects.get(user=request.user)
    except UserDetail.DoesNotExist:
        user_detail = None

 
    return render(request, 'displayprofile.html', {'user_detail': user_detail})

  

def profile_edit(request,user_id):
    try:
        user_detail = UserDetail.objects.get(id=user_id,user=request.user)
    except UserDetail.DoesNotExist:
        user_detail = UserDetail(user=request.user)
    
    if request.method == 'POST':
        form = UserDetailForm(request.POST, request.FILES ,instance=user_detail)
        if form.is_valid():
            form.save()
            return redirect('displayprofile')  # Redirect to profile view after editing
    else:
        form = UserDetailForm(instance=user_detail)
    
    return render(request, 'editprofile.html', {'form': form})

 