from django.shortcuts import render,redirect
from django.http import HttpResponse
from web_01.models import User
from django.http import JsonResponse
# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, 'index.html')

    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        # 在数据库中添加字段
        user=User.objects.create(username=username, password=password)

        return redirect('/login/')

def login(request):
    """登录View视图函数"""

    if request.method == 'GET':
        # 返回登录页面
        username = request.COOKIES.get('name')
        return render(request, 'login.html', context={'username': username})
    else:
        # 登录业务逻辑
        # 获取 username 和 password
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        # 进行用户名和密码校验
        try:
            # 根据 username 和 password 查询对应的用户是否存在，即进行用户名和密码校验
            # get 方法默认会利用查询到的数据创建一个对应的模型类对象，并将这个模型对象返回
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            # 如果 get 方法查询不到数据，会出现 `模型类.DoesNotExist` 异常
            # 用户名或密码错误
            return JsonResponse({'message': 'login failed'})
        else:
            # 用户名和密码正确
            response = JsonResponse({'message': 'login success'})
            if remember == 'true':
                response.set_cookie('username', username, max_age=14 * 24 * 3600)
