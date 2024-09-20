from django.db import models


class Transaction(models.Model):
    brand_id = models.IntegerField()
    user_name = models.CharField(max_length=100)
    upload_time = models.DateTimeField(null=True,blank=True)
    receive_time = models.DateTimeField(null=True,blank=True)
    description = models.CharField(max_length=500)
    amount = models.DecimalField(max_digits=10, decimal_places=2)