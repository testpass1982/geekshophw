from django.urls import path, re_path
from . import views
import mainapp.views as mainapp
app_name = 'products'
urlpatterns = [
    re_path(r'^$', mainapp.products, name='category'),
    re_path(r'(?P<pk>\d+)/$', mainapp.products, name='category')
]