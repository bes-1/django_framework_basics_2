from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'title': 'Магазин'
    }
    return render(request, 'mainapp/index.html', context)


def products(request, name=None):
    context = {
        'category': ['Все', 'Дом', 'Офис', 'Модерн', 'Классика'],
        'title': 'Продукты',
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', context)
