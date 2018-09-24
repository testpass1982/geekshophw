from django.conf.urls import re_path

import basketapp.views as basketapp
app_name='basket'
urlpatterns = [
    re_path(r'^$', basketapp.basket, name='view'),
    re_path(r'^add/(?P<pk>\d+)/$', basketapp.basket_add, name='add'),
    re_path(r'^remove/(?P<pk>\d+)/$', basketapp.besket_remove, name='remove'),
    re_path(r'^edit/(?P<pk>\d+)/(?P<quantity>\d+)/$', basketapp.basket_edit, name='edit'),
]