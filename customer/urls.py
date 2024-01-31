from django.urls import path
from customer.serializer import CustomerSerializer,BusinessSerializer
from customer import views
from customer.models import Customer, Business
from .views import CustomerListCreateView,BusinessListCreateView


app_name = 'customer'

urlpatterns=[
    path('customer/', CustomerListCreateView.as_view(queryset=Customer.objects.all(), serializer_class=CustomerSerializer), name='user-list'),
    path('customer/<int:id>/',views.customer_details),
    path('business/<int:id>/',views.business_details),
    path('business/', BusinessListCreateView.as_view(queryset=Business.objects.all(), serializer_class=BusinessSerializer), name='business'),
]
