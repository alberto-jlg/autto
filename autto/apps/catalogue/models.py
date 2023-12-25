from django.db import models

# Create your models here.

class Automobile(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    price = models.IntegerField()
    mileage = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
