from django.contrib import admin

from catalog.models import Product, Category, Contact, Blog, Version
from users.models import User


@admin.action(description='Опубликовать выбранные товары')
def make_published(modeladmin, request, queryset):
    """ Публикует выбранные товары. """
    queryset.update(is_published=True)


@admin.action(description='Объявить продавцом администратора')
def set_admin(modeladmin, request, queryset):
    """ Ставит администратора владельцем товара. """
    user_admin = User.objects.get(is_superuser=True)
    queryset.update(creator=user_admin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Отображение товара в административной панели. """
    list_display = ('id', 'title', 'price', 'category', 'is_published',)
    list_filter = ('category',)
    search_fields = ('title', 'description',)
    actions = [make_published, set_admin]


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    """ Отображение актуальной версии товара в административной панели. """
    list_display = ('product', 'version_number', 'title', 'is_active')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Отображение категории в административной панели. """
    list_display = ('id', 'title',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """ Отображение контактных данных в административной панели. """
    list_display = ('id', 'name', 'phone', 'email', 'message',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """ Отображение блоговых записей в административной панели. """
    list_display = ('id', 'title', 'description', 'creation_date', 'view_count',)
    list_filter = ('creation_date', 'view_count',)
