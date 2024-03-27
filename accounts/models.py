from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    full_name = models.CharField(max_length=255, default='')  
    company_name = models.CharField(max_length=255, default='')
   
    role_name = models.CharField(max_length=100, default=None, null=True)

    # Hide the built-in fields from AbstractUser
    
    first_name = None
    last_name = None
    is_active = None
    is_staff = None
    is_superuser = None
    last_login = None
    date_joined = None

    @property
    def groups(self):
        return Group.objects.none()

    @property
    def user_permissions(self):
        return Permission.objects.none()

    def __str__(self):
        return self.email

class Role(models.Model):
    account_id = models.IntegerField()
    role_name = models.CharField(max_length=100)
    description = models.TextField()
    active_status_id = models.IntegerField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.role_name






