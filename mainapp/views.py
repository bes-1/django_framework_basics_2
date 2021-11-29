from django.shortcuts import render

# Create your views here.
from mainapp.models import Product, ProductCategory


def index(request):
    products_list = Product.objects.all()[:4]
    context = {
        'title': 'Магазин',
        'products': products_list,
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    context = {
        'links_menu': links_menu,
        'title': 'Продукты',
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', context)
