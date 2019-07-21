from django.http import JsonResponse
from rest_framework import viewsets
from django.utils import timezone
from .models import Users
import re
import json
from django.core.serializers.json import DjangoJSONEncoder
from .serializers import BoardUsersSerializer
# api方法

#登录
class UserAction(viewsets.ModelViewSet):
    queryset=Users.objects.all()
    serializer_class = BoardUsersSerializer
    #登录
    @staticmethod
    def UserLogin(request):
        if request.method == "GET":
            # 获取用户写的username和password
            user_account = request.GET.get("account")
            user_password = request.GET.get("password")
            if Users.objects.filter(account=user_account).count() != 0:
                user = Users.objects.get(account=user_account)
                if user.password == user_password:
                    # 传session
                    request.session['created_at'] = json.dumps(user.created_at,cls=DjangoJSONEncoder)
                    request.session['account'] = user.account
                    request.session['username'] = user.name
                    request.session['user_id']=user.id
                    request.session['is_login'] = True
                    return JsonResponse({
                        'loginSuccess': True,
                        'loginMessage': 'login successfully!',
                        'account':user.account,
                        'username':user.name,
                        'is_login':'1',
                        'user_id':user.id
                    })
            return JsonResponse({
                'loginSuccess': False,
                'loginMessage': 'login failed!',
                'is_login':'0'
            })
    #注册
    @staticmethod
    def UserRegister(request):
        if request.method == "GET":
            # 获取用户注册信息
            user_name = request.GET.get("username")
            user_password = request.GET.get("password")
            user_account = request.GET.get("account")
            if Users.objects.filter(account=user_account).count() == 0:
                # 账号不重复则可以注册，否则失败
                if re.match(r'[_0-9a-zA-Z]{6,18}', user_account) and re.match(r'[_0-9a-zA-Z]{6,18}',
                                                                              user_password) and re.match(
                        r'[_0-9a-zA-Z]{4,20}', user_name):
                    # 账号 密码 用户名符合要求则通过，否则失败
                    Users.objects.create(name=user_name, password=user_password, account=user_account,
                                         created_at=timezone.now())
                    return JsonResponse({
                        'registerSuccess': '1',
                        'registerMessage': 'register successfully!'
                    })
                else:
                    return JsonResponse({
                        'registerSuccess': '0',
                        'registerMessage': 'register failed!you need to '
                                           'check the format of your account,password or username!'
                    })
            else:
                return JsonResponse({
                    'registerSuccess': '2',
                    'registerMessage': 'this account already exists!'
                })
    @staticmethod
    def UserLogout(request):
        if request.method=='GET':
            user_account=request.session['account']
            boarduser_id=request.session['user_id']
            if Users.objects.filter(account=user_account,id=boarduser_id).count()!=0:
                request.session['created_at'] =''
                request.session['account'] = ''
                request.session['username'] = ''
                request.session['user_id'] = ''
                request.session['is_login'] = False,
                return JsonResponse({
                    'logoutSuccess':True,
                    'message':'logout successfully!'
                })
            else:
                return JsonResponse({
                    'logoutSuccess': False,
                    'message': 'you haven\'t login!'
                })