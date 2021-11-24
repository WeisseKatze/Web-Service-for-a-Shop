from rest_framework import serializers
from ..models import Order, OrderItem
from shop.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    cost = serializers.DecimalField(max_digits=10, decimal_places=2, source = 'get_cost', read_only = True)
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity','cost']
    
    def create(self, validated_data):
        product_data = validated_data.pop('product')
        return OrderItem.objects.create(product = product_data['name'], price = product_data['price']  **validated_data)


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    total_cost = serializers.DecimalField(max_digits=10, decimal_places=2, source = 'get_total_cost', read_only = True)
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 
                  'email', 'address', 'postal_code', 'city', 
                  'created', 'updated', 'items', 'total_cost']

