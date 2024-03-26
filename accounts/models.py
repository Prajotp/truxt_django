from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    account_id = models.IntegerField(default=None, null=True)
    full_name = models.CharField(max_length=255, default='')  
    company_name = models.CharField(max_length=255, default='')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    user_type_id = models.IntegerField(default=None, null=True)
    invitation_id = models.IntegerField(default=None, null=True)
    role_id = models.IntegerField(default=None, null=True)

    def __str__(self):
        return self.username


    def __str__(self):
        return self.username

