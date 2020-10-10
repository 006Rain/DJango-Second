from datetime import datetime
from django.db import models

class Custormer( models.Model ):
    name = models.CharField( max_length=200 )
    phone_number = models.CharField( max_length=200 )
    address = models.CharField( max_length=200 )

class Medicine( models.Model ):
    name = models.CharField( max_length=200 )
    serial_number = models.CharField( max_length=200 )
    desc = models.CharField( max_length=200 )

class Order( models.Model ):
    name = models.CharField( max_length=200, null=True, blank=True )
    create_date = models.DateTimeField( default=datetime.now )
    customer = models.ForeignKey( Custormer, on_delete=models.PROTECT )
    medicines = models.ManyToManyField( Medicine, through="OrderMedicine" )

class OrderMedicine( models.Model ):
    order = models.ForeignKey( Order, on_delete=models.PROTECT )
    medicine = models.ForeignKey( Medicine, on_delete=models.PROTECT )
    medicine_count = models.PositiveIntegerField()