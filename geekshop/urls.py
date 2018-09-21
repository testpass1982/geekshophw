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
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
import mainapp.views as mainapp
from mainapp.models import ProductCategory

urlpatterns = [
    path('', mainapp.main, name='main'),
    # path('mens/', mainapp.mens, name='mens'),
    # path('womens/', mainapp.womens, name='womens'),
    path('sale/', mainapp.sale, name='sale'),
    path('product/', mainapp.product, name='product'),
    path('new/', mainapp.new, name='new'),
    path('faq/', mainapp.faq, name='faq'),
    path('checkout/', mainapp.checkout, name='checkout'),
    path('admin/', admin.site.urls),
    re_path(r'^auth/', include('authapp.urls', namespace='auth')),
    re_path(r'^products/', include('mainapp.urls', namespace='products')),
    re_path(r'^basket/', include('basketapp.urls', namespace='basket')),
    re_path(r'^auth/verify/google/oauth2/', include("social_django.urls", namespace="social")),
    re_path(r'^order/', include('ordersapp.urls', namespace='order')),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)