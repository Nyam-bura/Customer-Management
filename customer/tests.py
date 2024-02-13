from django.test import TestCase
from django.urls import reverse
from customer.models import Customer

class CustomerTestCase(TestCase):

    def setUp(self):
        Customer.objects.create(name="Judy", contact_email='wanjiruujudy@gmail.com')

    def test_model_creation(self):
        """Test whether the model can be created properly"""
        obj = Customer.objects.get(name="Test Name")
        self.assertEqual(obj.contact_email, "Test contact_email")

    def test_view(self):
        """Test a view"""
        response = self.client.get(reverse('CustomerListCreateView'))
        self.assertEqual(response.status_code, 200)
 