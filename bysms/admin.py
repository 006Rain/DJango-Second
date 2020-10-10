from django.contrib import admin
from bysms.models import Custormer, Order, Medicine, OrderMedicine

# Register your models here.
admin.site.register( [Custormer, Order, Medicine, OrderMedicine] )