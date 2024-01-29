from django.db import models
from django.utils.translation import gettext as _


class Customer(models.Model):
    customer_name = models.CharField(_('customer_name'),max_length=100)
    contact_phone = models.CharField(_('contact_phone'),max_length=20)
    contact_email = models.EmailField(_('contact_email'))
    date_of_birth = models.DateField(_('date_of_birth'))
    nationality=models.CharField(_('nationality'),max_length=50)


class Business(models.Model):
    business_name =models.CharField(_('business_name'), max_length=100)
    business_categories =models.CharField(_('business_categories'),max_length=100)
    business_registration_date =models.DateField(_('business_registration'))
    age_of_business =models.DateField(_('age_of_business'))

class BusinessCategories(models.Model):
    id = models.AutoField(_('id'),primary_key=True)
    title = models.CharField(_('title'),max_length=100)  

