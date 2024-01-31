from rest_framework import serializers
from .models import Customer,Business

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model =Customer
        fields = '__all__'

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model =Business
        fields = '__all__'
