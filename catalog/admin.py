"""Модуль для работы с административной панелью."""
from django.contrib import admin
from catalog.models import Product, Category, Contact


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Отображение товара в административной панели."""
    list_display = ('id', 'title', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('title', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Отображение категории в административной панели."""
    list_display = ('id', 'title',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Отображение контактных данных в административной панели."""
    list_display = ('id', 'name', 'phone', 'email', 'message',)