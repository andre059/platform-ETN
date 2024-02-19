from rest_framework import serializers

from network.models import Supplier, Product, NetworkElement


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ('debt_to_supplier',)  # Запрет обновления поля "Задолженность перед поставщиком"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkElement
        fields = '__all__'
