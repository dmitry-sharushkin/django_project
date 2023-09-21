from django.shortcuts import render

from catalog.models import Category, Product


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории товаров'

    }
    return render(request, 'catalog/categories.html', context)


def products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category=pk),
        'title': f'Продукты {category_item.name}'

    }
    return render(request, 'catalog/products.html', context)

