from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from db.paginator_util import page_group
from db.search_db import *
from sys_user.models import *
from common import es_


# 系统管理/用户角色
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


# 系统管理/系统用户
class SysUseView(View):
    def get(self,request):
        if request.GET.get('id'):
            print(request.GET.get('id'))
            sysuse = SysUser.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': sysuse.id,
                'name':sysuse.name,
                'auth_string':sysuse.auth_string,
                'email':sysuse.email,
                'phone':sysuse.phone
            })
        sysuses = SysUser.objects.all()
        return render(request, 'sys_mgr/sysuser_list.html', locals())

    def post(self, request):
        id = request.GET.get("sysuser_id")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        print(id,name,phone)
        if id:
            sysuser = SysUser.objects.get(pk=id)
            sysuser.name = name
            sysuser.phone = phone
            sysuser.email = email
            sysuser.save()

        else:
            SysUser.objects.create(name=name,phone=phone,email=email)

        return redirect('/sysuse/')

    def delete(self, request):
        sysuser_id = request.GET.get('id')
        sysuser = SysUser.objects.get(pk=sysuser_id)
        sysuser.delete()

        return JsonResponse({
            "status":0,
            "msg":"删除成功"
        })


# 系统管理/用户权限
class UserAuthView(View):
    def get(self,request):
        auth_id = request.GET.get("id")
        if auth_id:
            userauth = Userauth.objects.get(pk=auth_id).auth
            if userauth == 0 and not Authdeatil.objects.filter(auth_id=auth_id):
                Authdeatil.objects.create(auth_id=auth_id,auth_deatil1="管理系统",auth_detail="不可以修改系统")
            elif userauth == 1 and not Authdeatil.objects.filter(auth_id=auth_id):
                Authdeatil.objects.create(auth_id=auth_id, auth_deatil1="管理系统", auth_detail="可以修改系统")
            authdeatil = Authdeatil.objects.get(pk=auth_id)
            return render(request, 'sys_mgr/user_auth.html', locals())

        auths = Userauth.objects.all()
        return render(request, 'sys_mgr/user_auth.html',locals())


# 数据表管理
class ShowTableView(View):
    def get(self, request):
        items = show_tables()
        chinese = show_tables()
        return render(request, 'sys_mgr/alltable.html', locals())


#  数据库管理/数据表管理/添加编辑删除
class Product_view(View):
    def get(self, request):
        table = request.GET.get('tname')
        tname = get_tname(table)
        pagenumber = request.GET.get('page',1)
        # 查询数据库
        items1, items2 = search_table(table)

        # 组装数据为列表
        items_list = package_items(items1, items2)
        # 分页
        page,page_list,paginator = page_group(pagenumber,items1)
        return render(request, 'sys_mgr/product.html', locals())

# 添加,编辑
    def post(self, request):
        table = request.GET.get('table')
        flag = request.GET.get('flag')
        value_dict = request.POST
        if flag == "1":
            sql = insert_sql(value_dict,table)
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

# 删除
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


# 模糊查询
class Serach_view(View):
    def post(self,request):
        table = request.GET.get("tname")
        pagenum = request.GET.get("page",1)
        items2 = desc_table(table)
        # 用post请求模糊查询
        str1 = request.POST.get("str")
        items = search_str(str1,table)
        items_list = package_items(items, items2)
        page,page_list,paginator = page_group(pagenum,items)
        return render(request, 'sys_mgr/product.html', locals())
    def get(self,request):
        table = request.GET.get("tname")
        pagenum = request.GET.get("page", 1)
        # 用get请求接参分页
        str1 = request.GET.get("str1", '')
        items2 = desc_table(table)
        items = search_str(str1, table)
        items_list = package_items(items, items2)
        page, page_list, paginator = page_group(pagenum, items)
        return render(request, 'sys_mgr/product.html', locals())


# 订单统计
class OrderView(View):
    def get(self,request):
        return render(request,'sys_mgr/order_status.html')


# 搜索引擎
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


# 日志
class ESLogView(View):
    def post(self, request):

        data = request.POST
        print(data)

        return JsonResponse({
            'status': 0,
            'msg': '上传日志成功'
        })