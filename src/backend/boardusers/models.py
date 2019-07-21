from django.db import models
from django.utils import timezone

class Users(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    account=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=timezone.now())
    updated_at=models.DateTimeField(default=timezone.now())