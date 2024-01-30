from django.db import models
from django.utils.translation import gettext as _
from model_utils import Choices
from django.utils import timezone

COUNTY_CHOICES = Choices(
    (1, 'BOMET', _('BOMET')),
    (2, 'Eldoret', _('Eldoret')),
)


class Customer(models.Model):
    customer_name = models.CharField(_('customer_name'),max_length=100)
    contact_phone = models.CharField(_('contact_phone'),max_length=20)
    contact_email = models.EmailField(_('contact_email'))
    date_of_birth = models.DateField(_('date_of_birth'))
    nationality=models.CharField(_('nationality'),max_length=50)


class Business(models.Model):
    business_name =models.CharField(_('business_name'), max_length=100)
    business_category = models.ForeignKey('customer.BusinessCategories', on_delete=models.CASCADE)  
    business_registration_date =models.DateField(_('business_registration'))
    county = models.PositiveSmallIntegerField(choices=COUNTY_CHOICES,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)

    @property
    def age_of_business(self):
        today = timezone.now().date()
        registration_date = self.business_registration_date
        age = today-registration_date
        return age.days
    
    def __str__(self):
        return f'{self.business_name}'



class BusinessCategories(models.Model):
    id = models.AutoField(_('id'),primary_key=True)
    title = models.CharField(_('title'),max_length=100)  

