from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products, CategoryListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/<int:pk>/', products, name='products'),
    path('product_card/<int:pk>/', ProductDetailView.as_view(), name='product_card')
]
