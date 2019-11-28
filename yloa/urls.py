from django import db
from django.http import HttpRequest
from django.urls import path
from common import make_pwd
from sys_user.views import *
from sys_user.views import RoleView, ESView, ESLogView


# 主页
def to_index(request: HttpRequest):
    return render(request, 'index.html', locals())


# 登陆
def to_login(request: HttpRequest):
    if request.method == "POST":
        # 获取用户名和口令
        name = request.POST.get('name', '')
        pwd = request.POST.get('pwd', '')
        if any((not name, not pwd, len(name) == 0, len(pwd) == 0)):
            error = '用户名或口令不能为空!'

        else:
            ret = SysUser.objects.filter(name=name, auth_string=make_pwd(pwd))
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


# 注册
def to_regist(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = SysUser.objects.create(name=username,auth_string=make_pwd(password))
        SysUserRole.objects.create(id=user.id,user_id=user.id,role_id=2)
        return redirect('/login/')
    return render(request, 'register.html')


# 登出
def to_logout(req: HttpRequest):
    req.session.pop('login_user')
    return redirect('/login/')


urlpatterns = [
    path('regist/', to_regist),
    path('login/', to_login),
    path('logout/', to_logout),
    path('role/', RoleView.as_view()),
    path('product/',Product_view.as_view()),
    path('search/',Serach_view.as_view()),
    path('init_es/', ESView.as_view()),
    path('upload_log/', ESLogView.as_view()),
    path('show_table/',ShowTableView.as_view()),
    path('order_status/',OrderView.as_view()),
    path('sysuse/', SysUseView.as_view()),
    path('userauth/', UserAuthView.as_view()),
    path('user_register/',User_register.as_view()),
    path('', to_index),
]
