from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone


NATIONALITY_CHOICES = [
    ("kenyan", "Kenyan"),
    ("ugandan", "Ugandan"),
    ("tanzanian", "Tanzanian"),
    ("rwandese", "Rwandese")
]
# unsaishi ajy vibasic ni kama kesho haiko promised 

class Customer(models.Model):
    customer_name = models.CharField(_('customer_name'),max_length=100)
    id_number = models.CharField(_('id_number'),max_length=20,unique=True)
    contact_phone = models.CharField(_('contact_phone'),max_length=20)
    contact_email = models.EmailField(_('contact_email'),unique=True)
    date_of_birth = models.DateField(_('date_of_birth'))
    nationality=models.CharField(_('nationality'),choices=NATIONALITY_CHOICES,max_length=50,null=True)

class Business(models.Model):
    business_name =models.CharField(_('business_name'), max_length=100)
    business_category = models.PositiveSmallIntegerField('business_category')  
    business_registration_date =models.DateField(_('business_registration'))
    county = models.ForeignKey('County', on_delete=models.CASCADE, null=True, related_name='businesses')
    customer = models.ForeignKey(Customer, default=1, verbose_name="customer", on_delete=models.SET_DEFAULT)
    building_name = models.CharField(max_length=100,null=True)
    sub_county = models.ForeignKey(_('SubCounty'),on_delete=models.CASCADE,null=True)
    ward = models.ForeignKey(_('Ward'),on_delete=models.CASCADE,null=True)
    floor = models.PositiveSmallIntegerField(null=True)




    @property
    def age_of_business(self):
        today = timezone.now().date()
        registration_date = self.business_registration_date
        age = today-registration_date
        return age.days
    
    def __str__(self):
        return f'{self.business_name}'
    
class County(models.Model):
    id = models.AutoField(_('id'),primary_key=True)
    county_name = models.CharField(_('name'),max_length=100)

class SubCounty(models.Model):
    id = models.AutoField(_('id'),primary_key=True)
    subcounty_name = models.CharField(_('name'),max_length=100) 

    def __str__(self):
        return self.subcounty_name
    
class Ward(models.Model):
    id = models.AutoField(_('id'),primary_key=True)
    ward_name= models.CharField(_('name'),max_length=100)  

    def __str__(self):
        return self.ward_name


class BusinessCategories(models.Model):
    id = models.AutoField(_('id'),primary_key=True)
    title = models.CharField(_('title'),max_length=100)