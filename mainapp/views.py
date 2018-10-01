from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductCategory, Product
from basketapp.models import Basket
from django.shortcuts import get_object_or_404
import json, os

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
    
# def mens(request):
#     return render(request, 'mainapp/products.html', mens_content)

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
            products = Product.objects.all()
            category = 'all'   
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).select_related('category')[:3]
            print(products.query)
        
        category = ProductCategory.objects.filter(pk=pk)
        content = {
            'title': category,
            'products': products,
            'links_menu': links_menu,
            'basket': basket,
        }
        return render(request, 'mainapp/products.html', content)
    
    same_products = Product.objects.all()[3:5]

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
    
