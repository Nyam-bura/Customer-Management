from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()
    date_of_birth = models.DateField()
    nationality=models.CharField(max_length=50)


class Business(models.Model):
    business_name = models.CharField(max_length=100)
    business_categories = models.CharField(max_length=100)
    business_registration_date = models.DateField()
    age_of_business = models.DateField()

