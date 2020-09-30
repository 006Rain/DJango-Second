from django.db import models

class Custormer( models.Model ):
    name = models.CharField( max_length=200 )
    phone_number = models.CharField( max_length=200 )
    address = models.CharField( max_length=200 )
    qq = models.CharField( max_length=30, null=True, blank=True )