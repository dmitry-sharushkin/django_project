from django.urls import path, re_path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, categories, products

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    re_path(r'^contacts', contacts, name='contacts'),
    re_path(r'^categories', categories, name='categories'),
    path('<int:pk>/products/', products, name='products'),
]
