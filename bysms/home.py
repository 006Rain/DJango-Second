import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from bysms.models import Custormer


def home( request ):
    return render( request, "signin.html" )
    # if "usertype" not in request.session:
    #     return render( request, "sign.html" )

    if request.session["usertype"] == "manager":
        return render( request, "manager.html" )
    else:
        return render( request, "sales.html" )




def list_customer( request ):
    print( "*" * 15 )
    print( "*" * 15 )
    customer_set = Custormer.objects.values()
    ret_list = list( customer_set )
    print( ret_list )
    return HttpResponse( json.dumps( {"ret":0, "ret_list":ret_list}, ensure_ascii=False ), content_type='application/json' )

def add_customer( request ):
    info = request.params["data"]
    ret_record = Custormer.objects.create( name=info["name"],
                            phone_number=info["phone_number"],
                            address=info["address"] )
    return JsonResponse( { "ret": 0, "id": ret_record.id } )

def modify_customer( request ):
    customer_id = request.params["id"]
    new_data = request.params["new_data"]
    try:
        custormer = Custormer.objects.get( id=customer_id )
    except Custormer.DoesNotExist:
        return JsonResponse( { "ret":1, "msg": f'id为{customer_id}的客户不存在！' } )

    if "name" in new_data:
        custormer.name = new_data["name"]
    if "phone_number" in new_data:
        custormer.phone_number = new_data["phone_number"]
    if "address" in new_data:
        custormer.address = new_data["address"]

    custormer.save()
    return JsonResponse( {"ret": 0} )

def del_customer( request ):
    customer_id = request.params["id"]
    try:
        customer = Custormer.objects.get( id=customer_id )
    except Custormer.DoesNotExist:
        return JsonResponse( { "ret": 1, "msg": f"id为{customer_id}的客户不存在！" } )

    customer.delete()
    return JsonResponse( { "ret": 0 } )


def dispatcher( request ):
    # Judge: if sign in with manager acount
    if "usertype" not in request.session:
        return render( request, "sign.html" )
    if request.session["usertype"] != "manager":
        return render( request, "sign.html" )

    return list_customer( request )

    # get http request params
    if request.method == "GET":
        request.params = request.GET
    elif request.method in ["POST", "PUT", "DELETE"]:
        request.params = json.load( request.body )

    action = request.params["action"]
    if action == "list_customer":
        return list_customer( request )
    elif action == "add_customer":
        return add_customer( request )
    elif action == "modify_customer":
        return modify_customer( request )
    elif action == "del_customer":
        return del_customer( request )
    else:
        return JsonResponse( { "ret": 1, "msg":"不支持该类型http请求" } )
