from .models import Customer,Business
from customer.serializer import CustomerSerializer, BusinessSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

class CustomerListCreateView(generics.ListCreateAPIView, APIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)
    

@api_view(['GET', 'PUT','PATCH', 'DELETE'])
def customer_details(request, id):
    try:
        customer_instance = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = CustomerSerializer(customer_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class BusinessListCreateView(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BusinessSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self,request,*args,**kwargs):
        id_number = request.data.get('id_number')
        customer = get_object_or_404(Customer,id_number=id_number)
        request.data["customer"]=customer.id
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['GET', 'PUT','PATCH', 'DELETE'])
def business_details(request, id):
    try:
        business_instance = Business.objects.get(pk=id)
    except Business.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BusinessSerializer(business_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BusinessSerializer(business_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = BusinessSerializer(business_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        business_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
