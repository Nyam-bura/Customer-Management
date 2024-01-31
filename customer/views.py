from django.shortcuts import render
from .models import Customer
from rest_framework import generics
from customer.serializer import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view




class CustomerListCreateView(generics.ListCreateAPIView):
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
        # Implement logic for updating the drink instance with request data
        serializer = CustomerSerializer(customer_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        # Implement logic for partially updating the drink instance with request data
        serializer = CustomerSerializer(customer_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        customer_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    # venye naeza create business and attach the customer

