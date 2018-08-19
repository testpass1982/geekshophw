from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=150)
    manufacturer = models.CharField(max_length=70)
    size = models.IntegerField(default=0)
    date_added = models.DateTimeField(blank=True, null=True)
    in_catalog = models.BooleanField(default=False, verbose_name="Show in catalog?")

    def __str__(self):
        return self.title
