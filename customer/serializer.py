from rest_framework import serializers
from .models import Customer,Business,BusinessCategories

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model =Customer
        fields = '__all__'

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model =Business
        fields = '__all__'


class BusinesscategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCategories    
        fields = '__all__'   