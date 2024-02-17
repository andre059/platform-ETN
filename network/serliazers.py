from rest_framework import serializers

from network.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ('debt_to_supplier',)  # Запрет обновления поля "Задолженность перед поставщиком"
