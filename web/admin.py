from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin
from web.models import Supplier, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'email', 'country', 'city',
                    'street', 'house', 'supplier_of_link',
                    'debt', 'created_at',)
    list_filter = ('city',)
    search_fields = ('name', 'level', 'email', 'country', 'city',
                     'street', 'house', 'supplier_of',
                     'debt', 'created_at',)
    actions = ['clear_debt']

    def supplier_of_link(self, obj):
        """Метод для создания кликабельной ссылки на ссылаемый объект"""
        if obj.supplier_of:
            url = reverse('admin:%s_%s_change' % (obj.supplier_of._meta.app_label, obj.supplier_of._meta.model_name),
                          args=[obj.supplier_of.pk])
            return format_html('<a href="{}">{}</a>', url, obj.supplier_of.name)
        return '-'

    supplier_of_link.short_description = 'Поставщик'


    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
        self.message_user(request, "Задолженность перед поставщиком была обнулена")
    clear_debt.short_description = "Обнулить задолженность"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'created_at',)
    search_fields = ('name', 'model', 'created_at',)