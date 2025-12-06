from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class Register(AbstractUser):
    usertype=models.CharField(max_length=100,null=True,default='admin')
    imag=models.FileField(upload_to='profile_image',null=True)
    phone_number=models.PositiveIntegerField(default=0,null=True)
