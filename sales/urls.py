from django.urls import path
import sales.views

urlpatterns = [
    path( "", sales.views.index ),
    path( "customers/", sales.views.list_customers )
]
