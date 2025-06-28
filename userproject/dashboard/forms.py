from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DocumentVersion, Task, UserDetail,Message




class SignUpForm(UserCreationForm):
    email=forms.EmailField(max_length=254,help_text='Required .Imform a valid email address.')

    class Meta:
        model=User
        fields =('username','email','password1','password2')





class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['firstname', 'lastname', 'contact', 'address','profile_photo']



class TaskForm(forms.ModelForm):
    document = forms.FileField(required=False)
    class Meta:
        model = Task
        fields = ['receiver', 'title','description']

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = DocumentVersion
        fields = ['document', 'version_note']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']