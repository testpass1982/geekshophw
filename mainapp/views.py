from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductCategory, Product
from basketapp.models import Basket
from django.shortcuts import get_object_or_404
import json, os
from django.conf import settings
from django.core.cache import cache
from django.views.decorators.cache import cache_page

with open('static/new_products.json', 'r', encoding='UTF-8') as p:
    new_products_json = p.read()
    new_products = json.JSONDecoder().decode(new_products_json)

links_menu = [
    {'href': 'main', 'name':'home'},
    # {'href': '/mens', 'name':'mens'},
    # {'href': '/womens', 'name':'womens'},
    # {'href': '/kids', 'name':'kids'},
    {'href': 'faq', 'name':'faq'},
    {'href': 'sale', 'name':'sale items'},
]

# def get_links_menu():
#     if settings.LOW_CACHE:
#         key = 'links_menu'
#         links_menu = cache.get(key)
#         if links_menu is None:
#             links_menu = ProductCategory.objects.filter(is_active=True)
#             # print(links_menu)
#             cache.set(key, links_menu)
#         return links_menu
#     else:
#         return ProductCategory.objects.filter(is_active=True)

def category_to_menu_dict (category_pk, category_name):
    return {'pk': category_pk, 'name': category_name}

menu_category_start = 1
for category in ProductCategory.objects.all():
    links_menu.insert(menu_category_start, category_to_menu_dict(category.pk, category.name.lower()))
    menu_category_start+=1

content = {
    'products': Product.objects.all(),
    'links_menu': links_menu,
    'title': 'rubernLaces',
}

print(links_menu)
print("**********************************************************")
print(content)

# Create your views here.

def get_category(pk):
    if settings.LOW_CACHE:
        key = 'category_{}'.format(pk)
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)

def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).select_related('category')

def get_products_orederd_by_price():
   if settings.LOW_CACHE:
       key = 'products_orederd_by_price'
       products = cache.get(key)
       if products is None:
           products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
           cache.set(key, products)
       return products
   else:
       return Product.objects.filter(is_active=True, category__is_active=True).order_by('price')

def get_products_in_category_orederd_by_price(pk):
   if settings.LOW_CACHE:
       key = 'products_in_category_orederd_by_price_{}'.format(pk)
       products = cache.get(key)
       if products is None:
           products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')
           cache.set(key, products)
       return products
   else:
       return Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')

def test(request, category):
    print(category)
    return HttpResponse("This is the test")

def index(request):
    return HttpResponse("Hello, this is mainapp index")

def main(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        content['basket'] = basket
    return render(request, 'mainapp/index.html', content)
    
def checkout(request):
    return render(request, 'mainapp/checkout.html', content)

@cache_page(3600)
def products(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    print(basket)
    print('len of basket', len(basket))
    print("BASKET ***********************")
    print(pk)
    title = 'All products'
    if pk:
        if pk == '0':
            products = get_products()
            category = 'all'   
        else:
            # category = get_object_or_404(ProductCategory, pk=pk)
            category = get_category(pk) #get cached categories
            products = Product.objects.filter(category__pk=pk).select_related('category')[:3]
            # products = get_products_in_category_orederd_by_price(pk)
            print(products.query)
        
        # category = ProductCategory.objects.filter(pk=pk)
        category = get_category(pk)
        content = {
            'title': category,
            'products': products,
            'links_menu': links_menu,
            # 'links_menu': get_links_menu(),
            'basket': basket,
        }
        return render(request, 'mainapp/products.html', content)
    
    same_products = Product.objects.all()[3:5].select_related()

    content = {
        'title': title,
        'products': same_products,
          'links_menu': links_menu,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', content)

def new(request):
    return render(request, 'mainapp/new.html', content)
    
def product(request):
    return render(request, 'mainapp/product.html', content)
    
def sale(request):
    return render(request, 'mainapp/sale.html', content)
    
def faq(request):
    return render(request, 'mainapp/faq.html', content)

def login(request):
    return render(request, 'mainapp/login.html', content)
    

