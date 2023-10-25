from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Category, Product


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/categories.html'


# class ProductsDetailView(DetailView):
#     model = Product
#     template_name = 'catalog/products_detail.html'


def products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category=pk),
        'title': f'Продукты {category_item.name}'

    }
    return render(request, 'catalog/products_detail.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_card.html'
