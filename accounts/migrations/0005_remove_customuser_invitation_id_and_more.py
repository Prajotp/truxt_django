# Generated by Django 5.0.2 on 2024-03-27 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_remove_customuser_date_joined_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="customuser", name="invitation_id",),
        migrations.RemoveField(model_name="customuser", name="user_type_id",),
    ]
