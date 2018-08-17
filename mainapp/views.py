from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, this is mainapp index")

def main(request):
    return render(request, 'mainapp/index.html')
    
def checkout(request):
    return render(request, 'mainapp/checkout.html')
    
def mens(request):
    return render(request, 'mainapp/mens.html')
    
def womens(request):
    return render(request, 'mainapp/womens.html')
    
def new(request):
    return render(request, 'mainapp/new.html')
    
def product(request):
    return render(request, 'mainapp/product.html')
    
def sale(request):
    return render(request, 'mainapp/sale.html')
    
def faq(request):
    return render(request, 'mainapp/faq.html')
    
