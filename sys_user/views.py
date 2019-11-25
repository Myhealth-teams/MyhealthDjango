from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from db.search_db import *
from sys_user.models import *
from common import es_





#系统管理/用户角色

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


# 数据表管理
class ShowTableView(View):
    def get(self, request):
        items = show_tables()
        return render(request, 'sys_mgr/alltable.html', locals())


#  数据库管理/数据表管理
class Product_view(View):
    def get(self, request):
        table = request.GET.get('tname')
        items1, items2 = search_table(table)
        items_list = package_items(items1, items2 )
        return render(request, 'sys_mgr/product.html', locals())

    def post(self, request):
        table = request.GET.get('table')
        flag = request.GET.get('flag')
        print(table,flag)
        value_dict = request.POST
        print(value_dict)
        if flag == "1":
            sql = insert_sql(value_dict,table)
            print(sql)
            if insert_field(sql):
                print("添加成功")
            else:
                print("添加失败")
        elif flag == '0':
            sql = update_sql(value_dict,table)
            print(sql)
            if insert_field(sql):
                print("编辑成功")
            else:
                print("编辑失败")

        return redirect('/product/?tname='+table)

    def delete(self, request):
        id = request.GET.get("d_id")
        table_name = request.GET.get("tname")
        str_id = request.GET.get("str_id")
        print(str_id)
        str_delete = str_id +"="+id
        sql = "delete from {} where {}".format(table_name, str_delete)
        print(sql)
        if insert_field(sql):
            return JsonResponse({
                'status': 0,
                'msg': '删除成功!'
            })
        else:
            return JsonResponse({
                'status':1,
                'msg':'删除失败！'
            })


#搜索引擎和日志
class ESView(View):
    def get(self, request):
        # 同步ES（初始化）
        es_.create_index()

        cursor = connection.cursor()
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