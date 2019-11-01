from django.db import models

class project(models.Model):
    class Meta:
        verbose_name = "项目表"
        db_table = 'project'
    project_name=models.CharField('项目名称',max_length=80)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
#项目里面配环境

class environment(models.Model):
    class Meta:
        verbose_name = "环境表"
        db_table = 'environment'
    host_name=models.CharField('环境名称',max_length=80)
    host_v=models.CharField('地址',max_length=80)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
#加项目id

class modset(models.Model):
    class Meta:
        verbose_name = "模块配置表"
        db_table = 'modset'
    mod_name=models.CharField('模块名称',max_length=80)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)


class testcase(models.Model):
    class Meta:
        verbose_name = "测试用例表"
        db_table = 'testcase'
    e_id=models.IntegerField("环境id")
    p_id=models.IntegerField("项目id")
    m_id=models.IntegerField("模块id")
    case_name=models.CharField('用例名称',max_length=100)
    interface=models.CharField('接口地址',max_length=100)
    request_mode=models.CharField('请求方式',max_length=100)
    parameter=models.CharField('请求参数',max_length=100)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
#加一个断言，参数传递

class config(models.Model):
    class Meta:
        verbose_name = "配置表"
        db_table = 'config'

    config_name=models.CharField('配置名称',max_length=80)
    config_info=models.CharField('配置内容',max_length=80)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
