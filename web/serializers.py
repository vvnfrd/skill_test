from rest_framework import serializers

from web.models import Product, Supplier


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'


    def validate_debt(self, value):
        if self.instance and value != self.instance.debt:
            raise serializers.ValidationError("Нельзя обновлять параметр задолженности перед поставщиком")
        return value