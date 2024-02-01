from django.db import models
from django.utils.translation import gettext as _
from model_utils import Choices
from django.utils import timezone

COUNTY_CHOICES = Choices(
    (1, 'NAIROBI', _('NAIROBI')),
    (2, 'MOMBASA', _('MOMBASA')),
)

SUB_COUNTY_CHOICES = (
    (1, 'WESTLANDS', _('WESTLANDS')),
    (2, 'LIKONI', _('LIKONI'))
)
WARD_CHOICES = (
    (1, 'MAKONGENI', _('MAKONGENI')),
    (2, 'MTONGWE', _('MTONGWE'))
)

BUSINESSCATEGORIES_CHOICES = Choices(
    (1, 'SMALL SCALE', _('SMALL SCALE')),
    (2, 'LARGE SCALE', _('LARGE SCALE')),
)

NATIONALITY_CHOICES = (
    ("kenyan", "kenyan"),
    ("ugandan", "ugandan"),
    ("tanzanian", "tanzanian"),
    ("rwandees", "rwandees")
)

class Customer(models.Model):
    customer_name = models.CharField(_('customer_name'),max_length=100)
    id_number = models.CharField(_('id_number'),max_length=20,unique=True)
    contact_phone = models.CharField(_('contact_phone'),max_length=20)
    contact_email = models.EmailField(_('contact_email'),unique=True)
    date_of_birth = models.DateField(_('date_of_birth'))
    nationality=models.CharField(_('nationality'),choices=NATIONALITY_CHOICES,max_length=50,null=True)

class Business(models.Model):
    business_name =models.CharField(_('business_name'), max_length=100)
    business_category = models.PositiveSmallIntegerField('business_category',choices=BUSINESSCATEGORIES_CHOICES)  
    business_registration_date =models.DateField(_('business_registration'))
    county = models.CharField(_('county'),max_length=100,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    building_name = models.CharField(max_length=100,null=True)
    sub_county = models.CharField(_('sub_county'),max_length=100,null=True)
    ward = models.CharField(_('ward'),max_length=50,null=True)
    floor = models.PositiveSmallIntegerField(null=True)

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



    
