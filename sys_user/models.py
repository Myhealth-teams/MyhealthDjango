# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Carts(models.Model):
    c_id = models.AutoField(primary_key=True)
    u = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    goods = models.ForeignKey('Goods', models.DO_NOTHING, blank=True, null=True)
    c_goods_num = models.IntegerField()
    c_is_selected = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'carts'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Goods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=256)
    price = models.FloatField()
    medtype = models.IntegerField()
    standards = models.CharField(max_length=30)
    detial = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods'
    def __str__(self):
        return "商品表"



class Medtypes(models.Model):
    m_id = models.AutoField(primary_key=True)
    typenum = models.IntegerField()
    medname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'medtypes'



class RotationStatus(models.Model):
    rs_id = models.AutoField(primary_key=True)
    ro = models.ForeignKey('Rotatitons', models.DO_NOTHING, blank=True, null=True)
    rs_name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'rotation_status'


class Rotatitons(models.Model):
    ro_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'rotatitons'




class SysRole(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'sys_role'



class SysUser(models.Model):
    name = models.CharField(unique=True, max_length=50)
    auth_string = models.CharField(max_length=100)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return "%s %s %s %s" % (self.name, self.auth_string, self.email, self.phone)

    @property
    def role(self):
        role_id = SysUserRole.objects.get(id=self.id).role_id
        return SysRole.objects.get(pk=role_id)

    class Meta:
        managed = False
        db_table = 'sys_user'



class SysUserRole(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_role'


class Users(models.Model):
    u_name = models.CharField(max_length=20, blank=True, null=True)
    u_password = models.CharField(max_length=50)
    u_tel = models.CharField(unique=True, max_length=11)
    u_image = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

class Authdeatil(models.Model):
    detail_id = models.AutoField(primary_key=True)
    auth_deatil1 = models.CharField(max_length=50, blank=True, null=True)
    auth_detail = models.CharField(max_length=50, blank=True, null=True)
    auth_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authdeatil'

class Userauth(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    auth = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userauth'