from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseForbidden

from .models import Task, UserDetail
from .forms import SignUpForm,UserDetailForm
from .models import Task, DocumentVersion, Message
from .forms import TaskForm, DocumentUploadForm, MessageForm, SignUpForm
from django.utils.timezone import now

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request.user)
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
        return redirect('editprofile', user_id=request.user.id)

    sent = Task.objects.filter(sender=request.user)
    received = Task.objects.filter(receiver=request.user)

    return render(request, 'displayprofile.html', {
        'user_detail': user_detail,
        'sent': sent,
        'received': received
    })


  

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

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.sender = request.user
            task.save()
            if request.FILES.get('document'):
             DocumentVersion.objects.create(
                task=task,
                uploaded_by=request.user,
                document=request.FILES['document']
            )
            return redirect('displayprofile')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.user != task.sender and request.user != task.receiver:
        return redirect('dashboard')

    docs = DocumentVersion.objects.filter(task=task).order_by('timestamp')
    messages = Message.objects.filter(task=task).order_by('timestamp')

    if request.method == 'POST':
        doc_form = DocumentUploadForm(request.POST, request.FILES)
        msg_form = MessageForm(request.POST)
        if 'document' in request.FILES and doc_form.is_valid():
            doc = doc_form.save(commit=False)
            doc.task = task
            doc.uploaded_by = request.user
            doc.save()
        if msg_form.is_valid():
            msg = msg_form.save(commit=False)
            msg.task = task
            msg.sender = request.user
            msg.save()
        return redirect('task_detail', pk=pk)

    doc_form = DocumentUploadForm()
    msg_form = MessageForm()
    return render(request, 'task_detail.html', {
        'task': task,
        'docs': docs,
        'messages': messages,
        'doc_form': doc_form,
        'msg_form': msg_form,
    })

@login_required
def mark_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.user == task.receiver:
        task.is_completed = True
        task.completed_at = now()
        task.save()
    return redirect('task_detail', pk=pk)