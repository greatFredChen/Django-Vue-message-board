from django.urls import path, include
from . import  views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('boardusers',views.UserAction) #使用router管理api路由情况！

app_name='BoardUsers'
urlpatterns=[
    path('userLogin', views.UserAction.UserLogin,name='UserLogin'),
    path('userRegister', views.UserAction.UserRegister,name='UserRegister'),
    path('userLogout',views.UserAction.UserLogout,name='UserLogout'),
    path('',include(router.urls))
]