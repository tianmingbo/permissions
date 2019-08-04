def init_session(user_obj, request):
    # 查询当前用户有哪些权限
    print(user_obj)
    role_list = user_obj.roles.all()
    permission_list = []
    for i in role_list:
        permission = i.peimissions.all().values('url')
        for j in permission:
            permission_list.append(j)
    request.session['permission_list'] = permission_list
