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



class Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    description = models.TextField()
    
    def __str__(self):
        return self.name
