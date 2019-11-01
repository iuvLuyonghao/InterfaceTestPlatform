#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 16:59
# @Author  : 
# @File    : sqlcontrol.py
# @Software: PyCharm

from  AutoTest.models import *
from django.db import connection
import json
class sqlcontrol:

    def __init__(self,datainfo_dict=None,sql=None):
        self.datainfo_dict=datainfo_dict
        self.sql=sql
    def insert_eir(self):
        environmentinfo=environment(host_name=self.datainfo_dict['eirname'],host_v=self.datainfo_dict['eirurl'])
        environmentinfo.save()
    def select_eir(self):
        # cursor=connection.cursor()
        # cursor.execute("select * from environment order by create_time desc")
        # row=cursor.fetchone()
        # return row
        # return environment.objects.raw("select * from environment order by create_time desc")
        datas=environment.objects.order_by("-id")
        return datas

    def insert_project(self):
        projentinfo=project(project_name=self.datainfo_dict['projectname'])
        projentinfo.save()
    def select_project(self):
        datas=project.objects.order_by("-id")
        return datas

    def insert_mod(self):
        projectinfo=project(mod_name=self.datainfo_dict['modname'])
        projectinfo.save()
    def select_mod(self):
        datas=modset.objects.order_by("-id")
        return datas

    def insert_case(self):
        print(self.datainfo_dict)
        caseinfo=testcase(p_id=self.datainfo_dict['project'],
                          e_id=self.datainfo_dict['eir'],
                          m_id=self.datainfo_dict['model'],
                          case_name=self.datainfo_dict['casename'],
                          interface=self.datainfo_dict['interface'],
                          request_mode=self.datainfo_dict['requestmethon'],
                          parameter=self.datainfo_dict['requestdata']
                          )
        caseinfo.save()
    def select_case(self):
        datas=testcase.objects.order_by("-id")
        return datas

    def run_sql(self):
        cursor=connection.cursor()
        cursor.execute(self)
        row=cursor.fetchone()
        # row=testcase.objects.raw(self)
        return row
if __name__=='__main__':
    sqlcontrol().select_eir()