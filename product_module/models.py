from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    name=models.CharField(max_length=100)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.name


class Category(models.Model): 
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    quantity=models.IntegerField()
    image_url=models.CharField(max_length=500)
    color_code=models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    category=models.ForeignKey(Category,on_delete=models.CASCADE) 
    registered_on = models.DateTimeField() 
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def image_tag(self): 
        return mark_safe(f'<img src="{self.image_url}" width="50"  height="50" />') 

class CartItem(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    entered_on = models.DateTimeField()

    def __str__(self):
        return self.product.name

