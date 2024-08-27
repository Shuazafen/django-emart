from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
      return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=55)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.ImageField(upload_to="product_image")
    quantity = models.IntegerField()

    def __str__(self):
      return self.name

class CartItem(models.Model):
    #id = models.AutoField(primary_key=True)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()

    def cost(self):
        self.total = self.Product.price * self.quantity

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()

    def sum(self):
        self.amount = sum(self.item for self.item in self.item.total)