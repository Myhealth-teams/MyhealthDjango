#!/usr/bin/python3
# coding: utf-8
from django.http import HttpRequest
from django.shortcuts import redirect


def valid_login(view_func):
    not_valid_paths = ['/login/', '/regist/', '/upload_log/']
    def wrapper(request: HttpRequest, *args, **kwargs):
        print('--valid_login---', request.path)

        # 验证当前请求是否在登录之后
        if all((
                'login_user' not in request.session.keys(),
                 request.path not in not_valid_paths
                )):
            return redirect('/login/')

        return view_func(request, *args, **kwargs)

    return wrapper