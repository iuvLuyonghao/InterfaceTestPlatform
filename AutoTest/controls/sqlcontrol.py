#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 16:59
# @Author  : 
# @File    : sqlcontrol.py
# @Software: PyCharm

from  AutoTest.models import *

class sqlcontrol:

#注册
    def register(self,userinfo_dict):
        print(userinfo_dict)
        userinfo = User(company=userinfo_dict['company'], realname=userinfo_dict['realname'], username=userinfo_dict['username'], password=userinfo_dict['password'], phone=userinfo_dict['phone'], email=['email'])
        userinfo.save()


if __name__=='__main__':
    sqlcontrol().register()