from django.contrib import admin
from .models import Manufacturer, Product, ProductCategory
from authapp.models import ShopUser
from basketapp.models import Basket
from ordersapp.models import Order
# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(ShopUser)
admin.site.register(Basket)
admin.site.register(Order)
