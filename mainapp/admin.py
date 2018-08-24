from django.contrib import admin
from .models import Manufacturer, Product, ProductCategory
# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Manufacturer)
admin.site.register(Product)
