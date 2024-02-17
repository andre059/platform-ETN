from django.contrib import admin

from network.models import Supplier, Product, NetworkElement


@admin.action(description='Очистить задолженность')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)
    clear_debt.short_description = 'Очистить задолженность перед поставщиком'


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number')
    list_filter = ('name', 'email', 'country', 'city', 'street', 'house_number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'debt_to_supplier', 'created_at', 'debt')
    list_filter = ('name', 'model', 'release_date', 'debt_to_supplier', 'created_at')
    actions = [clear_debt]


@admin.register(NetworkElement)
class NetworkElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'country', 'city', 'street', 'house_number', 'level', 'element_type', 'debt')
    list_filter = ['city']
    actions = [clear_debt]
