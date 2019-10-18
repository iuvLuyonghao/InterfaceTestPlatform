from django.shortcuts import render

# Create your views here.
from  django.http import HttpResponse
from  django.shortcuts import render
from  .models import  User

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
    return render(request, 'index.html')
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
        userinfo_list=[company,realname,username,password,phone,email]
        for date in  userinfo_list:
            if date is None or date =='':
                empty_data=True
        if empty_data == True:
            print('请检查全部必填项')
            return render(request, "result.html",context={"msg":"请填写全部必填项"})
        elif password != repassword:
            print("请验证两次密码是否一致")
            return render(request, "result.html",context={"msg":"请验证两次密码是否一致"})
        else:
            #入库
            userinfo=User(company=company,realname=realname,username=username,password=password,phone=phone,email=email)
            userinfo.save()
            return render(request,'result.html',context={"msg":"注册成功"})
    elif request.method == 'GET':
        return render(request,"register.html")

#登录接口
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        users=User.objects.all()
        for user in users:
            if user.username==username and user.password==password:
                print("登录成功")
                return render(request,'index.html')
            else:
                print("登录失败")
                return render(request, 'login.html')
    elif request.method== 'GET':
        return render(request,'login.html')


