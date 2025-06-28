from django.db import models
from django.contrib.auth.models import User,AbstractUser


# Create your models here.
class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    address = models.TextField(null=True)
    profile_photo = models.ImageField(upload_to='profilephotos/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s details"



class Task(models.Model):
    sender=models.ForeignKey(User,related_name='sent_tasks',on_delete=models.CASCADE)
    receiver=models.ForeignKey(User,related_name='received_tasks',on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.TextField()
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    completed_at=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.title} ({self.sender.username} → {self.receiver.username})"
    


class DocumentVersion(models.Model):
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    uploaded_by=models.ForeignKey(User,on_delete=models.CASCADE)
    document=models.FileField(upload_to='documents/',blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    version_note=models.TextField(blank=True)


class Message(models.Model):
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    sender=models.ForeignKey(User,on_delete=models.CASCADE)   
    text=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)





 