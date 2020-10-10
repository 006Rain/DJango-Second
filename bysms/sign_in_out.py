import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

def signup( request ):
    user_name = request.POST.get( "username" )
    password1 = request.POST.get( "password1" )
    password2 = request.POST.get( "password2" )
    return render( request, "signup.html" )
    #

    user = authenticate( username=user_name, password=password1 )

    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login( request, user )
                request.session["usertype"] = "manager"
                return redirect( "/" )
            else:
                return JsonResponse( {"ret":1, "msg":"请使用管理员账户登录！"} )
        else:
            return JsonResponse( {"ret":0, "msg":"账户已被禁用！"} )
    else:
        return JsonResponse( {"ret":1, "msg":"用户名或密码错误！"} )
    pass

def signin( request ):
    user_name = request.POST.get( "username" )
    password = request.POST.get( "password" )
    user = authenticate( username=user_name, password=password )

    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login( request, user )
                request.session["usertype"] = "manager"
                return redirect( "/" )
            else:
                return JsonResponse( {"ret":1, "msg":"请使用管理员账户登录！"} )
        else:
            return JsonResponse( {"ret":0, "msg":"账户已被禁用！"} )
    else:
        return JsonResponse( {"ret":1, "msg":"用户名或密码错误！"} )
    pass

def signout( request ):
    logout( request )
    return JsonResponse( {"ret": 0} )