from django.db import models

# Create your models here.

class Pago(models.Model):
    amount = models.IntegerField(default=0)
    currency_code = models.CharField(max_length=5)
    description = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    source_id = models.CharField(max_length=200)