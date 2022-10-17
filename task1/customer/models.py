from django.db import models

class customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.DecimalField(max_digits=2, decimal_places=0)
    created_in = models.DateTimeField(auto_now=True)
