from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.views import View
<<<<<<< HEAD

from common import es_
from sys_user.models import *

=======
from pymysql.cursors import DictCursor

from sys_user.models import SysRole
>>>>>>> c4571bae774ff3624468a72c53c7febd78fc4a22

from django.db import connection

# Create your views here.

<<<<<<< HEAD
#系统管理/用户角色
=======
from common import es_

>>>>>>> c4571bae774ff3624468a72c53c7febd78fc4a22
class RoleView(View):
    def get(self, request):
        if request.GET.get('id', ''):
            role = SysRole.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': role.id,
                'name': role.name,
                'code': role.code
            })

        roles = SysRole.objects.all()
        return render(request, 'sys_mgr/role_list.html', locals())

    def post(self, request):
        print(request.POST)
        id = request.POST.get('role_id', None)  # 注意： form表单页面不建议使用id 字段名
        name = request.POST.get('name')
        code = request.POST.get('code')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            role = SysRole.objects.get(pk=id)

            role.name = name
            role.code = code  # 建议不修改code
            role.save()
        else:
           SysRole.objects.create(name=name, code=code)

        return redirect('/role/')

    def delete(self, request):
        role_id = request.GET.get('id')
        role = SysRole.objects.get(pk=role_id)
        role.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })


<<<<<<< HEAD
#产品管理/产品分类
class Product_view(View):
    def get(self, request):
        if request.GET.get('id', ''):
            goods = Goods.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': goods.id,
                'name': goods.name,
                'url': goods.url,
                'price':goods.price,
                'medtype':goods.medtype,
                'standards':goods.standards,
                'detial':goods.detial
            })

        goods = Goods.objects.all()
        return render(request, 'sys_mgr/product.html', locals())
    def post(self, request):
        print(request.POST)
        id = request.POST.get('goods_id', None)  # 注意： form表单页面不建议使用id 字段名
        name = request.POST.get('goods_name')
        url = request.POST.get('url')
        price = request.POST.get('price')
        medtype = request.POST.get('medtype')
        standards = request.POST.get('standards')
        detial = request.POST.get('detial')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            good = Goods.objects.get(pk=id)
            good.goods_name = name
            good.url = url
            good.price = price
            good.medtype = medtype
            good.standards = standards
            good.detial = detial
            good.save()
        else:
           Goods.objects.create(goods_name=name, url=url,price=price,medtype=medtype,standards=standards,detial=detial)

        return redirect('/product/')

    def delete(self, request):
        goods_id = request.GET.get('id')
        good = SysRole.objects.get(pk=goods_id)
        good.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })


#搜索引擎和日志
=======
>>>>>>> c4571bae774ff3624468a72c53c7febd78fc4a22
class ESView(View):
    def get(self, request):
        # 同步ES（初始化）
        es_.create_index()

        cursor = connection.cursor()
<<<<<<< HEAD
        cursor.execute('select * from goods')
        for row in cursor.fetchall():
            print(row)
            doc = {
                'id': row[0],
                'name': row[1],
                'url': row[2],
                'price': row[3],
                'medtype': row[4],
                'standards': row[5],
                'detial': row[6]
=======
        cursor.execute('select id,name,ord_sn,parent_id from t_category')
        for row in cursor.fetchall():
            doc = {
                'id': row[0],
                'name': row[1],
                'ord_sn': row[2],
                'parent_id': row[3]
>>>>>>> c4571bae774ff3624468a72c53c7febd78fc4a22
            }

            es_.add_doc(doc, 'category')

        return JsonResponse({
            'status': 0,
            'msg': '同步ElasticSearch搜索引擎成功'
        })


class ESLogView(View):
    def post(self, request):

        data = request.POST
        print(data)

        return JsonResponse({
            'status': 0,
            'msg': '上传日志成功'
        })