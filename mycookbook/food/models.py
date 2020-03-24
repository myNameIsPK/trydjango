from django.db import models

# Create your models here.
class Food(models.Model):
    title       = models.CharField(max_length=100) #max_length must have
    description = models.TextField(blank=True,null=True) #null = in DB can or cannot null
    materials   = models.TextField(blank=False,null=False)
    price       = models.DecimalField(max_digits=7, decimal_places=2) #example 10,000.00