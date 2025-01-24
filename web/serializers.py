from rest_framework import serializers
from web.models import Product, Supplier


class ProductSerializer(serializers.ModelSerializer):
    """ Сериализатор продуктов """

    class Meta:
        model = Product
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    """ Сериализатор поставщиков """

    class Meta:
        model = Supplier
        fields = '__all__'

    def validate_debt(self, value):
        """ Запрет на обновление задолженности перед поставщиком через API """

        if self.instance and value != self.instance.debt:
            raise serializers.ValidationError("Нельзя обновлять параметр задолженности перед поставщиком")
        return value
