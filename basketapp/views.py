from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product
from mainapp.views import links_menu
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

@login_required
def basket(request):
    def _get_product_cost(self):
        return self.product.price * self.quantity
    
    product_cost = property(_get_product_cost)

    def _get_total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity

    total_quantity = property(_get_total_quantity)

    def _get_total_cost(self):
        _items = Basket.objects.filter(user=self.user)
        _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return _totalcost

    total_cost = property(_get_total_cost)

    content = { 'title': 'basket',
                'links_menu': links_menu,
                'product_cost': product_cost,                
                'total_quantity': total_quantity,
                'total_cost': total_cost,
}

    return render(request, 'basketapp/basket.html', content)

@login_required
def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    old_basket_item = Basket.objects.filter(user=request.user, product=product)

    if old_basket_item:
        old_basket_item[0].quantity +=1
        old_basket_item[0].save()

    else:
        new_basket_item = Basket(user=request.user, product=product)
        new_basket_item.quantity +=1
        new_basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def besket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()

        else:
            new_basket_item.delete()

        basket_items = Basket.objects.filter(user=request.user).order_by('product__price')

        content = {
            'basket' : basket_items,
        }

        result = render_to_string('basketapp/includes/inc_basket_list.html', content)

        return JsonResponse({'result': result})