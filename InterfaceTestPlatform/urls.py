"""InterfaceTestPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  AutoTest.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',index),
    path(r'index/',index),
    path(r'project_setting/',project_setting),
    path(r'case_setting/',case_setting),
    path(r'model_setting/',model_setting),
    path('system_setting/',system_setting),
    path('eir_setting/',eir_setting)

]
