# Generated by Django 5.0.2 on 2024-03-26 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="account_id",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="company_name",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="customuser",
            name="full_name",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="customuser",
            name="invitation_id",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="role_id",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="user_type_id",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="password",
            field=models.CharField(max_length=100),
        ),
    ]