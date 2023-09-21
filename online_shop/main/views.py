from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'main/index.html')

def create(request):
    return render(request, 'main/create.html')

def shop(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'main/shop.html', context)


