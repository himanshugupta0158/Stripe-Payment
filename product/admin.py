from django.contrib import admin

from .models import Product , Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id' , 'ordered_on']
