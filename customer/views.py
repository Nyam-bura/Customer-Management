from django.shortcuts import render
from .models import Customer
from rest_framework import generics
from customer.serializer import CustomerSerializer
from rest_framework.response import Response


class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)
    

    # venye naeza create business and attach the customer
    
