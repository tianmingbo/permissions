from django.shortcuts import render, HttpResponse,redirect
from rbac import models
from rbac.service.permissions import *


# Create your views here.
def users(request):
    return HttpResponse('users')


def add_user(request):
    return HttpResponse('add_user')


def delete_user(request):
    return HttpResponse('delete_user')


def roles(request):
    return HttpResponse('roles')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user_obj = models.User.objects.filter(name=username, pwd=pwd).first()

        if user_obj:
            # 如果登陆成功，吧用户信息写入session
            request.session['user_id'] = user_obj.pk
            # print(request.session['user_id'])
            # 查询当前登陆用户的权限，写入session
            init_session(user_obj, request)
            return redirect('/users/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')
