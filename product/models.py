from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents
    

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

class Order(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    ordered_on = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.product)