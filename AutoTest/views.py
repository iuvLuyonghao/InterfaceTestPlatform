from django.shortcuts import render

# Create your views here.
from  django.http import HttpResponse
from  django.shortcuts import render
from  AutoTest.controls.sqlcontrol import  sqlcontrol
from django.shortcuts import render_to_response


#首页
def index(request):
    # if request.method=='GET':
    return render_to_response("index.html")
#环境配置
def eir_setting(request):
    if request.method=='POST':
        eirname=request.POST.get('eirname','')
        eirurl=request.POST.get('eirurl','')
        eirlist={'eirname':eirname,'eirurl':eirurl}
        sqlcontrol(eirlist).insert_eir()
        datas=sqlcontrol().select_eir()
        return render(request, 'eir_setting.html', {"datas":datas})
    elif request.method=='GET':
        datas=sqlcontrol().select_eir()
        return render(request, 'eir_setting.html', {"datas":datas})

#项目配置
def project_setting(request):
    if request.method=='POST':
        projectname=request.POST.get('projectname','')
        eirlist={'projectname':projectname}
        sqlcontrol(eirlist).insert_project()
        datas=sqlcontrol().select_project()
        return render(request, 'project_setting.html', {"datas":datas})
    elif request.method=='GET':
        datas=sqlcontrol().select_project()
        return render(request, 'project_setting.html', {"datas":datas})

#模块配置
def model_setting(request):
    if request.method=='POST':
        modname=request.POST.get('modname','')
        eirlist={'modname':modname}
        sqlcontrol(eirlist).insert_project()
        datas=sqlcontrol().select_project()
        return render(request, 'model_setting.html', {"datas":datas})
    elif request.method=='GET':
        datas=sqlcontrol().select_project()
        return render(request, 'model_setting.html', {"datas":datas})



#用例配置
def case_setting(request):
    if request.method=='POST':
        project=request.POST.get('project','')
        eir=request.POST.get('eir','')
        model=request.POST.get('model','')
        casename=request.POST.get('casename','')
        interface=request.POST.get('interface','')
        requestmethod=request.POST.get('requestmethod','')
        requestdata=request.POST.get('requestdata','')
        datas={'project':project,'eir':eir,'model':model,'casename':casename,'interface':interface,'requestmethon':requestmethod,'requestdata':requestdata}
        print(datas)
        sqlcontrol(datas).insert_case()
        return render(request, 'case_setting.html', {"datas":datas})
    elif request.method=='GET':
        datas=sqlcontrol().select_case()
        return render(request, 'case_setting.html', {"datas":datas})




#系统配置
def system_setting(request):
    return  render_to_response("system_setting.html")




