import email
from django.db import models

# Create your models here.

class AdminLogin(models.Model):
    username=models.CharField(max_length=120)
    password=models.CharField(max_length=100)

    class Meta:
        db_table="admin_login"

class AddStudent(models.Model):
  
    name=models.CharField(max_length=120)
    contact=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    class Meta:
        db_table="add_student"