from django.urls import path, re_path

from catalog.views import home, contacts

urlpatterns = [
    path('', home),
    re_path(r'^contacts', contacts),
]
