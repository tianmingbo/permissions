from django.shortcuts import render, HttpResponse
from rbac import models
from rbac.service.permissions import *


# Create your views here.
def users(request):
    pass


def add_user(request):
    pass


def delete_user(request):
    pass


def roles(request):
    pass


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
            print(init_session(user_obj, request))
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')
