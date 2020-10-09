from django.urls import path
from medicine_salse_sys import manager, sign_in_out

urlpatterns = [
    path( "", manager.dispatcher ),
    path( "signin/", sign_in_out.signin ),
    path( "signout/", sign_in_out.signout ),
]
