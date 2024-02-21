# class CustomerTestCase(TestCase):

#     def setUp(self):
#         Customer.objects.create(name="Judy", contact_email='wanjiruujudy@gmail.com')

#     def test_model_creation(self):
#         """Test whether the model can be created properly"""
#         obj = Customer.objects.get(name="Judy")  
#         self.assertEqual(obj.contact_email, "wanjiruujudy@gmail.com") 

#     def test_view(self):
#         """Test a view"""
#         response = self.client.get(reverse('CustomerListCreateView'))
#         self.assertEqual(response.status_code, 200)
from django.test import TestCase
from django.core.exceptions import ValidationError
from customer.models import Customer

class CustomerModelTestCase(TestCase):

    def test_customer_creation(self):
        """Test whether the Customer model can be created properly"""

        # Create a customer instance
        customer = Customer.objects.create(
            customer_name="John Doe",
            id_number="20012002",
            contact_phone="0790500842",
            contact_email="john@gmail.com",
            date_of_birth="1990-01-01",
            nationality="kenyan"
        )

        # Retrieve the customer from the database
        saved_customer = Customer.objects.get(id=customer.id)

        self.assertEqual(saved_customer.customer_name, "John Doe")
        self.assertEqual(saved_customer.id_number, "20012002")
        self.assertEqual(saved_customer.contact_phone, "0790500842")
        self.assertEqual(saved_customer.contact_email, "john@gmail.com")
        self.assertEqual(saved_customer.date_of_birth, "1990-01-01")
        self.assertEqual(saved_customer.nationality, "kenyan")

    def test_unique_id_number(self):
        """Test whether the id_number field is unique"""

        Customer.objects.create(
            customer_name="Jane Doe",
            id_number="30908070",
            contact_phone="0729837078",
            contact_email="jane@gmail.com",
            date_of_birth="2000-02-11",
            nationality="ugandan"
        )

        with self.assertRaises(ValidationError):
            Customer.objects.create(
                customer_name="Jane Doe",
                id_number="30908070",
                contact_phone="0729837078",
                contact_email="jane@gmail.com",
                date_of_birth="2000-02-11",
                nationality="ugandan"
            )

