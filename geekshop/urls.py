"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('mens/', mainapp.mens, name='mens'),
    path('womens/', mainapp.womens, name='womens'),
    path('sale/', mainapp.sale, name='sale'),
    path('product/', mainapp.product, name='product'),
    path('new/', mainapp.new, name='new'),
    path('faq/', mainapp.faq, name='faq'),
    path('checkout/', mainapp.checkout, name='checkout'),
    path('login/', mainapp.login, name='login'),
    path('admin/', admin.site.urls),
]
