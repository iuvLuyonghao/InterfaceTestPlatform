# Generated by Django 2.0.3 on 2019-10-31 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoTest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=80, verbose_name='环境名称')),
                ('host_v', models.CharField(max_length=80, verbose_name='地址')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '环境表',
                'db_table': 'environment',
            },
        ),
        migrations.CreateModel(
            name='modset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mod_name', models.CharField(max_length=80, verbose_name='模块名称')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '模块配置表',
                'db_table': 'modset',
            },
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=80, verbose_name='项目名称')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '项目表',
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='testcase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_id', models.IntegerField(max_length=65532, verbose_name='环境id')),
                ('p_id', models.IntegerField(max_length=65532, verbose_name='项目id')),
                ('m_id', models.IntegerField(max_length=65532, verbose_name='模块id')),
                ('case_name', models.CharField(max_length=100, verbose_name='用例名称')),
                ('interface', models.CharField(max_length=100, verbose_name='接口地址')),
                ('request_mode', models.CharField(max_length=100, verbose_name='请求方式')),
                ('parameter', models.CharField(max_length=100, verbose_name='请求参数')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '测试用例表',
                'db_table': 'testcase',
            },
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Progect',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='config',
            name='style',
        ),
        migrations.AddField(
            model_name='config',
            name='config_info',
            field=models.CharField(default='', max_length=80, verbose_name='配置内容'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='config',
            name='config_name',
            field=models.CharField(default='', max_length=80, verbose_name='配置名称'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='config',
            table='config',
        ),
    ]
