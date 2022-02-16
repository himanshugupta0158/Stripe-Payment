from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0.00 , max_digits=5 , decimal_places=2) #Rupees
    
    def __str__(self) :
        return self.name