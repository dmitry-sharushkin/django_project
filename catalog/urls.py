from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products, CategoryListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('catalog/create/', ProductCreateView.as_view(), name='create_product'),
    path('product_list/<int:pk>/', products, name='list_product'),
    path('product_card/<int:pk>/', ProductDetailView.as_view(), name='product_card'),
    path('catalog/edit/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('catalog/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]
