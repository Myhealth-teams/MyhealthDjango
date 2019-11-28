# !/usr/bin/env python
# -*-coding:UTF-8-*-
# __author__ = pighui
# __time__ = 2019-11-28 下午3:23
from yloa.settings import PORT,HOST
import os
if __name__ == '__main__':
    os.system("python manage.py runserver %s:%s"%(HOST,PORT))