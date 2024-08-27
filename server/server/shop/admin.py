from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields =['name']
    list_filter = ['name']

class ProductAdmin(admin.ModelAdmin) :
    list_display = ['id','name', 'description', 'category', 'price', 'image','quantity']
    search_fields = ['name', 'price', 'category']
    list_filter = ['id']

class CartItemAdmin(admin.ModelAdmin) :
    list_display = ['quantity', 'total']
    search_fields = ['product']

class CartAdmin(admin.ModelAdmin) :
    list_display = ['id', 'item', 'user', 'amount']
    search_fields = ['user', 'item']
    readonly_fields = ['user']
    list_filter = ['item']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart, CartAdmin)