from django.contrib import admin

from network.models import Product, Supplier, NetworkElement
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    list_filter = ('first_name', 'last_name')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number')
    list_filter = ('name', 'email', 'country', 'city', 'street', 'house_number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'debt_to_supplier', 'created_at')
    list_filter = ('name', 'model', 'release_date', 'debt_to_supplier', 'created_at')


@admin.register(NetworkElement)
class NetworkElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'country', 'city', 'street', 'house_number', 'level', 'element_type')
    list_filter = ('name', 'contact_email', 'country', 'city', 'street', 'house_number', 'level', 'element_type')
