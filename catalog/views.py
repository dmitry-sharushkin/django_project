from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Version


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/categories.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:categories')

    def form_valid(self, form):
        self.object = form.save()
        self.object.save
        return super().form_valid(form)


def products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category=pk),
        'title': f'Продукты {category_item.name}'

    }
    return render(request, 'catalog/product_list.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_card.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_card', args=[self.object.pk])

    def form_valid(self, form):
        self.object = form.save()
        self.object.save
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:categories')


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self):
        return reverse('catalog:product_card', args=[self.object.product.pk])
