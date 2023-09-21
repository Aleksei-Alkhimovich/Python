from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('shop', views.shop, name='shop'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_items'),
]
