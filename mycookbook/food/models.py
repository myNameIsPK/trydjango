from django.db import models

# Create your models here.
class Food(models.Model):
    title       = models.TextField()
    description = models.TextField()
    materials   = models.TextField()