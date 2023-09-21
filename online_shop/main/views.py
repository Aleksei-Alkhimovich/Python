from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView


def index(request):
    return render(request, 'main/index.html')


class NewsDetailView(DetailView):
    model = Product
    template_name = 'main/detail_items.html'
    context_object_name = 'article'


def shop(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'main/shop.html', context)
