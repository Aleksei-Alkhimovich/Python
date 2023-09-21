from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('shop', views.shop, name='shop'),
]
