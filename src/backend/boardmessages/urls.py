from django.urls import path, include
from . import  views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('boardmessages',views.MessageAction) #使用router管理api路由情况！

urlpatterns=[
    path('MessageIndex', views.MessageAction.MessageIndex,name='MessageIndex'),
    path('WriteMessage',views.MessageAction.WriteMessage,name='WriteMessage'),
    path('Like',views.MessageAction.Like,name='Like'),
    path('Dislike',views.MessageAction.Dislike,name='Dislike'),
    path('',include(router.urls))
]