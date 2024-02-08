from django.db import models

# Create your models here.
class Wish(models.Model):
    website=models.CharField(max_length=250)
    password=models.CharField(max_length=1000)
    def __str__(self):
        return  self.wishtitle