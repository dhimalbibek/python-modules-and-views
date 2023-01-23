from django.db import models

# Create your models here.
class Information(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.CharField(max_length=200)
