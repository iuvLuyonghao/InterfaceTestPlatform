from django.db import models

# Create your models here.
from django.db import models

#用户表
class User(models.Model):
    class Meta:
        verbose_name = "用户信息表"
        db_table = 'User'
    company = models.CharField("",max_length=80)
    realname = models.CharField("真实姓名",max_length=25)
    username = models.CharField("用户名",max_length=25)
    password = models.CharField("密码",max_length=18)
    phone = models.CharField("手机号",max_length=25)
    email = models.EmailField("邮箱",max_length=25)
    jurisdiction = models.CharField("权限",max_length=10)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

class Company(models.Model):
    class Meta:
        verbose_name = "公司信息表"
        db_table = 'Company'
    companyname=models.CharField("公司名称",max_length=25)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)


class Progect(models.Model):
    class Meta:
        verbose_name = "项目表"
        db_table = 'Progect'
    prpject=models.CharField("项目名称",max_length=25)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)



class Config(models.Model):
    class Meta:
        verbose_name = "配置表"
        db_table = 'Config'
    style=models.CharField("配置类型",max_length=10)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

class Report(models.Model):
    verbose_name = "测试报告表"
    db_table = 'Report'
reportname = models.CharField("报告名称", max_length=10)
create_time = models.DateTimeField('创建时间', auto_now_add=True)
update_time = models.DateTimeField('更新时间', auto_now=True)
