from django.shortcuts import render
from django.http import HttpResponse
from common.models import Custormer

# Create your views here.
def index( request ):
    return HttpResponse( "Index" )

def list_customers( request ):
    customer_set = Custormer.objects.values()
    phone_num = request.GET.get( "phone_number", None )
    qq_no = request.GET.get( "qq", None )
    if phone_num:
        print( "filter by phone_number ..." )
        customer_set = customer_set.filter( phone_number=phone_num )
    if qq_no:
        customer_set = customer_set.filter( qq=qq_no )

    ret_str = ""
    for customer in customer_set:
        for key, value in customer.items():
            ret_str += f"{key}:{value} | "
        ret_str += "<br/><br/>"
    return HttpResponse( ret_str )
