# user_app/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    USER_TYPES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    first_name=models.CharField(max_length=100,null=False, blank=False)
    last_name=models.CharField(max_length=100 ,null=False, blank=False)
    username=models.CharField(max_length=100,null=False, blank=False , unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    
    groups = models.ManyToManyField('auth.Group', related_name='myuser_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='myuser_user_permissions')
    
