'''
自定义中间件，校验是否有session
'''
import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse


def reg(request, current_path):
    # 获取所有权限
    url = request.session.get("permission_list")
    flag = False
    for permission in url:
        permission = "^%s$" % permission
        ret = re.match(permission, current_path)
        if ret:
            flag = True
            break
    return flag


class ValidPermission(MiddlewareMixin):
    def process_request(self, request):
        # 当前访问路径
        current_path = request.path_info

        # 这些路径不用校验
        valid_url_list = ['/login/', '/reg/', '/admin/.*']

        for valid_url in valid_url_list:
            ret = re.match(valid_url, current_path)
            if ret:
                return None

        # 校验是否登录
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect('/login/')
        flag = reg(request, current_path)  # 获取是否有权限
        if not flag:
            return HttpResponse("没有权限！")
        else:
            return None
