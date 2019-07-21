from django.db import models
from django.utils import timezone
from boardusers.models import Users
# Create your models here.

#user message本身
class User_Message(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=300)
    created_by=models.IntegerField()
    created_at=models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    thump_up_count=models.IntegerField()
    thump_down_count=models.IntegerField()

#点赞模块
class Like_And_Dislke(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.IntegerField()
    user_message_id=models.IntegerField()
    status=models.IntegerField(default=0)
    created_at=models.DateTimeField(default=timezone.now())
    User_Messages=models.ForeignKey('User_Message',on_delete=models.CASCADE,related_name='user_messages',default='')
    Users=models.ForeignKey('boardusers.Users',on_delete=models.CASCADE,related_name='users',default='')