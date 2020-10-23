from django.shortcuts import render, redirect
from django.http import HttpResponse
from web_01.models import User
from django.http import JsonResponse
from django.views import View


# 登录页面视图

class LoginView(View):
    #GET

    def get(self,request):
        # 判断用户是否登录
        username = request.session.get('username')
        if username:
            return HttpResponse('%s用户已登录' % username)

        # 若用户未登录，返回登录页面
        return render(request,'login.html')

    def post(self,request):
        # 注册页面
        # 先判断用户是否已经登录
        username = request.session.get('username')
        if username:
            return HttpResponse('%s用户已登录' % username)

        # 获取页面post返回的数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        # 查询数据库，判断用户名和密码是否正确
        try:
            # 根据 username 和 password 查询对应的用户是否存在，即进行用户名和密码校验
            # get 方法默认会利用查询到的数据创建一个对应的模型类对象，并将这个模型对象返回
            user=User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            # 如果 get 方法查询不到数据，会出现 `模型类.DoesNotExist` 异常
            # 用户名或密码错误
            return JsonResponse({'message': 'login failed'})
        else:
            # 用户名和密码正确
            request.session['user_id']=user.id
            request.session['username']=user.username

            if remember != 'true':
                # 表示不记住登录状态，设置 session 的有效期
                request.session.set_expiry(0)

            response=JsonResponse({'message': 'login success'})

            return response


def register(request):
    if request.method == 'GET':
        return render(request, 'index.html')

    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        # 在数据库中添加字段
        user=User.objects.create(username=username, password=password)

        return redirect('/login/')

#
# def login(request):
#     """登录View视图函数"""
#     """登录View视图函数"""
#     # 判断是否已经登录
#     username=request.session.get('username')
#
#     if username:
#         # username 在 session 中存在，则用户已登录
#         return HttpResponse('%s用户已登录' % username)
#
#     if request.method == 'GET':
#         # 返回登录页面
#         username=request.COOKIES.get('name')
#         return render(request, 'login.html', context={'username': username})
#     else:
#         # 登录业务逻辑
#         # 获取 username 和 password
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         remember=request.POST.get('remember')
#
#         # 进行用户名和密码校验
#         try:
#             # 根据 username 和 password 查询对应的用户是否存在，即进行用户名和密码校验
#             # get 方法默认会利用查询到的数据创建一个对应的模型类对象，并将这个模型对象返回
#             user=User.objects.get(username=username, password=password)
#         except User.DoesNotExist:
#             # 如果 get 方法查询不到数据，会出现 `模型类.DoesNotExist` 异常
#             # 用户名或密码错误
#             return JsonResponse({'message': 'login failed'})
#         else:
#             # 用户名和密码正确
#             request.session['user_id']=user.id
#             request.session['username']=user.username
#
#             if remember != 'true':
#                 # 表示不记住登录状态，设置 session 的有效期
#                 request.session.set_expiry(0)
#
#             response=JsonResponse({'message': 'login success'})
#
#             return response
