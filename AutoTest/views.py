from django.shortcuts import render

# Create your views here.
from  django.http import HttpResponse
from  django.shortcuts import render
from  .models import  User
from  AutoTest.controls import  sqlcontrol

sqlcon=sqlcontrol.sqlcontrol()
#首页
def index(request):
    # 判断是否是post请求
    if request.method == 'POST':
        # 获取到请求参数， username的写法，如果username不存在不会抛异常
        # password 会抛异常
        username = request.POST.get('username')
        password = request.POST['password']
        print(username,password)
        # 业务 需求：
        # users = []
        # for x in range(0, 3):
        #     users.append(
        #         {'username': '%s-%d' % (username, x), 'password': '%s-%d' % (password, x)}
        #     )
        #
        # # 返回给用户  模版中使用到的users就是这里传递进去的
        # return render(request, template_name='index.html', context={
        #     'users': users
        # })
    return render(request, 'base.html')
#注册接口
def register(request):
    empty_data=False
    if request.method == 'POST':
        company = request.POST.get('company')
        realname = request.POST.get('realname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        if password != repassword:
            print("请验证两次密码是否一致")
            return render(request, "result.html",context={"msg":"请验证两次密码是否一致"})
        else:
            #入库
            userinfo_list = {'company': company, 'realname': realname, 'username': username, 'password': password, 'phone': phone,
                             email: email}
            sqlcon.register(userinfo_list)
            return render(request,'result.html',context={"msg":"注册成功"})
    elif request.method == 'GET':
        return render(request,"register.html")

#登录接口
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            users=User.objects.all()
        except Exception as e:
            print(e)
        for user in users:
            if user.username==username and user.password==password:
                print("登录成功")
                return render(request,'index.html')
            else:
                print("登录失败")
                return render(request, 'login.html')
    elif request.method== 'GET':
        return render(request,'login.html')


def eircon(request):
    if request.method=='POST':
        print()
    elif request.method=='GET':
        return render(request,'index.html')

