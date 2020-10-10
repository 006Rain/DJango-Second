from django.urls import path
from bysms import home, sign_in_out

urlpatterns = [
    path( "", home.home ),
    path( "signup/", sign_in_out.signup ),
    path( "signin/", sign_in_out.signin ),
    path( "signout/", sign_in_out.signout ),
]
