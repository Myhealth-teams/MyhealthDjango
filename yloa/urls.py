from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import path

from sys_user.models import SysUser
from common import make_pwd
<<<<<<< HEAD:yloa/urls.py
from sys_user.views import *
=======
from sys_user.views import RoleView, ESView, ESLogView
>>>>>>> c4571bae774ff3624468a72c53c7febd78fc4a22:jyoa/urls.py


def to_index(request: HttpRequest):
    return render(request, 'index.html', locals())


def to_login(request: HttpRequest):
    if request.method == "POST":
        # 获取用户名和口令
        name = request.POST.get('name', '')
        pwd = request.POST.get('pwd', '')
        print('name=',name)
        print('pwd=',pwd)
        if any((not name, not pwd, len(name) == 0, len(pwd) == 0)):
            error = '用户名或口令不能为空!'

        else:
            print("--------")
            ret = SysUser.objects.filter(name=name, auth_string=make_pwd(pwd))
            print(ret)
            if ret.exists():
                login_user = ret.first()

                # 将登录的用户信息存在session中
                request.session['login_user'] = {
                    'id': login_user.id,
                    'name': login_user.name,
                    'role_name': login_user.role.name,
                    'role_code': login_user.role.code
                }

                return redirect('/')

            error = "用户名或口令错误!"

    return render(request, 'login.html', locals())


def to_regist(request: HttpRequest):
    return render(request, 'register.html')


def to_logout(req: HttpRequest):
    req.session.pop('login_user')
    return redirect('/login/')


urlpatterns = [
    path('regist/', to_regist),
    path('login/', to_login),
    path('logout/', to_logout),
    path('role/', RoleView.as_view()),
<<<<<<< HEAD:yloa/urls.py
    path('product/',Product_view.as_view()),
=======
>>>>>>> c4571bae774ff3624468a72c53c7febd78fc4a22:jyoa/urls.py
    path('init_es/', ESView.as_view()),
    path('upload_log/', ESLogView.as_view),
    path('', to_index),
]
