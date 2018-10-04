from django.db import models
from django.conf import settings
from mainapp.models import Product
from django.utils.functional import cached_property

class BasketQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)

class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)
    objects = BasketQuerySet.as_manager()
    
    # @cached_property
    def _get_product_cost(self):
        "return cost of all products this type"
        return self.product.price * self.quantity
    
    product_cost = property(_get_product_cost)
    
    @cached_property
    def get_items_cached(self):
        return self.user.basket_set.select_related('product')

    def _get_total_quantity(self):
        "return total quantity for user"
        _items = self.get_items_cached
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity
        
    total_quantity = property(_get_total_quantity)
    
    
    def _get_total_cost(self):
        "return total cost for user"
        _items = self.get_items_cached
        _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return _totalcost
        
    total_cost = property(_get_total_cost)
   
    @staticmethod
    def get_items(user):
        return user.basket_set.all()

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()