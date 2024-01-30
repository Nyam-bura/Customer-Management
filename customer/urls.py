from django.urls import path
from customer.serializer import CustomerSerializer
from customer.models import Customer

from .views import CustomerListCreateView

app_name = 'customer'

urlpatterns=[
    path('customer/', CustomerListCreateView.as_view(queryset=Customer.objects.all(), serializer_class=CustomerSerializer), name='user-list')
]