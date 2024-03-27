from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField(null=True)
    role_id = models.IntegerField()
    full_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=100)
    user_type_id = models.IntegerField()
    invitation_id = models.IntegerField(null=True)
    active_status_id = models.IntegerField()
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField(null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'