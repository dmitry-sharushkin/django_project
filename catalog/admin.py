from django.contrib import admin

from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'purchase_price', 'category',)
    list_filter = ('category',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'version_number', 'version_name', 'is_active')
    list_filter = ('product',)
    search_fields = ('product', 'version_number')
