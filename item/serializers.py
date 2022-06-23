from unicodedata import category
from numpy import source
from pyparsing import Or
from rest_framework import serializers
from item.models import Category, Item, Order, ItemOrder  

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]
        
        
class ItemSerializers(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Item
        fields = "__all__"
        
        
class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ItemSerializers(serializers.ModelSerializer):
    order = OrderSerializers(read_only=True)
    item_name = serializers.ReadOnlyField(source='item.name')        
    class Meta:
        model = ItemOrder
        fields = "__all__"
        
    
