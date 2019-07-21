from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.utils import timezone
from .models import User_Message,Like_And_Dislke
import re
from rest_framework import viewsets
from django.urls import reverse
from .serializers import BoardMessagesSerializers
from .serializers import Like_And_DisLikeSerializers
import json
from django.core.serializers.json import DjangoJSONEncoder
from boardusers.models import Users
# Create your views here.

class MessageAction(viewsets.ModelViewSet):
    queryset = User_Message.objects.all()
    serializer_class = BoardMessagesSerializers
    serializer_class_like=Like_And_DisLikeSerializers

    @staticmethod
    def MessageIndex(request):
        # TOPO 主页显示list
        if request.method=='GET':
            queryset=User_Message.objects.all()
            queryset_list=list(queryset)
            query_list=[]
            for item in queryset_list:
                username=Users.objects.get(id=item.created_by).name
                unitJson = {
                    'id':item.id,
                    'title':item.title,
                    'content':item.content,
                    'created_by':username,
                    'created_at':str(item.created_at),
                    'updated_at':str(item.updated_at),
                    'thump_up_count':item.thump_up_count,
                    'thump_down_count':item.thump_down_count
                }
                query_list.append(unitJson)

            return JsonResponse({
                'message_list':query_list
            })

    @staticmethod
    def Like(request):
        # TOPO 点赞
        if request.method=="GET":
            user_id = request.GET.get("user_id")
            user_message_id = request.GET.get("message_id")
            if Like_And_Dislke.objects.filter(user_id=user_id,user_message_id=user_message_id).count() == 0:
                user_message_object=User_Message.objects.get(id=user_message_id)
                count_up=user_message_object.thump_up_count+1
                User_Message.objects.filter(id=user_message_id).update(thump_up_count=count_up)
                user_message_object_alter = User_Message.objects.get(id=user_message_id)
                BoardUser = Users.objects.get(id=user_id)
                Like_And_Dislke.objects.create(user_id=user_id, user_message_id=user_message_id, status=1,
                                               User_Messages=user_message_object_alter,Users=BoardUser)
                return JsonResponse({
                    'messageSuccess':'1',
                    'message':'点赞成功'
                })
            else:
                return JsonResponse({
                    'messageSuccess': '2',
                    'message': '你已经点过赞或者踩，不可以再点啦!'
                })
        return JsonResponse({
            'messageSuccess': '0',
            'message': '点赞失败'
        })

    @staticmethod
    def Dislike(request):
        # TOPO 点踩
        if request.method == "GET":
            user_id = request.GET.get("user_id")
            user_message_id = request.GET.get("message_id")
            if Like_And_Dislke.objects.filter(user_id=user_id,user_message_id=user_message_id).count() == 0:
                user_message_object = User_Message.objects.get(id=user_message_id)
                count_down = user_message_object.thump_down_count + 1
                User_Message.objects.filter(id=user_message_id).update(thump_down_count=count_down)
                user_message_object_alter = User_Message.objects.get(id=user_message_id)
                BoardUser = Users.objects.get(id=user_id)
                Like_And_Dislke.objects.create(user_id=user_id, user_message_id=user_message_id,status=2,
                                               User_Messages=user_message_object_alter,Users=BoardUser)
                return JsonResponse({
                    'messageSuccess': '1',
                    'message': '点踩成功'
                })
            else:
                return JsonResponse({
                    'messageSuccess': '2',
                    'message': '你已经点过赞或者踩，不可以再点啦!'
                })
        return JsonResponse({
            'messageSuccess': '0',
            'message': '点踩失败'
        })

    @staticmethod
    def WriteMessage(request):
        # TOPO 写信息
        if request.method == 'GET':
            message_title=request.GET.get("title")
            message_content=request.GET.get("content")
            message_created_by=request.GET.get("user_id")
            User_Message.objects.create(title=message_title,content=message_content,
                                        created_by=message_created_by,thump_up_count=0,
                                        thump_down_count=0)
            return JsonResponse({
                'writeSuccess': True,
                'writeMessage': 'write message successfully!'
            })
        return JsonResponse({
            'writeSuccess': False,
            'writeMessage': 'write message failed!'
        })
