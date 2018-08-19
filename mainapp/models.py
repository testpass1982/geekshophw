from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=150)
    manufacturer = models.ManyToManyField("Manufacturer", related_name="products")
    size = models.IntegerField(default=0)
    date_added = models.DateTimeField(blank=True, null=True)
    in_catalog = models.BooleanField(default=False, verbose_name="Show in catalog?")

    def __str__(self):
        return self.title

class Manufacturer(models.Model):
    name = models.CharField(max_length=70, help_text="Use short name if possible", unique=True)

    def __str__(self):
        return self.name