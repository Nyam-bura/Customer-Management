from django.db import models
from django.utils.translation import gettext as _
from model_utils import Choices
from django.utils import timezone

COUNTY_CHOICES = Choices(
    (1, 'NAIROBI', _('NAIROBI')),
    (2, 'MOMBASA', _('MOMBASA')),
)

SUB_COUNTY_CHOICES = {
        'Nairobi': (
            ('Kasarani', 'Kasarani'),
            ('Westlands', 'Westlands'),
        ),
        'Mombasa': (
            ('Nyali', 'Nyali'),
            ('Likoni', 'Likoni'),
        ),
    }

WARD_CHOICES = {
        'Kasarani': (
            ('isipe', 'isipe'),
            ('Sunton', 'Sunton'),
            ('hunters', 'hunters')

        ),
        'Westlands': (
            ('Parklands', 'Parklands'),
            ('Spring Valley', 'Spring Valley'),
        ),
    }

FLOOR_CHOICES = (
        ('Ground Floor', 'Ground Floor'),
        ('1st Floor', '1st Floor'),
        ('2nd Floor', '2nd Floor'),
        ('3rd Floor', '3rd Floor'),
        ('4th Floor', '4th Floor'),
    )

BUILDING_CHOICES = {
    'Nairobi': (
        ('View Park Towers','view park Towers'),
        ('Kenyatta International Conference Centre (KICC)', 'Kenyatta International Conference Centre (KICC)'),
        ('Nation Centre', 'Nation Centre'),
    ),
    'Mombasa': (
        ('City Mall', 'City Mall'),
        ('Mombasa Beach Hotel', 'Mombasa Beach Hotel'),
        ('Nyali Centre', 'Nyali Centre'),
    ),
}


NATIONALITY_CHOICES = (
    ("kenyan", "kenyan"),
    ("ugandan", "ugandan"),
    ("tanzanian", "tanzanian"),
    ("rwandees", "rwandees")
)

class Customer(models.Model):
    customer_name = models.CharField(_('customer_name'),max_length=100)
    contact_phone = models.CharField(_('contact_phone'),max_length=20)
    contact_email = models.EmailField(_('contact_email'))
    date_of_birth = models.DateField(_('date_of_birth'))
    nationality=models.CharField(_('nationality'),choices=NATIONALITY_CHOICES,max_length=50,null=True)


class Business(models.Model):
    business_name =models.CharField(_('business_name'), max_length=100)
    business_category = models.ForeignKey('customer.BusinessCategories', on_delete=models.CASCADE)  
    business_registration_date =models.DateField(_('business_registration'))
    county = models.PositiveSmallIntegerField(choices=COUNTY_CHOICES,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    building_name = models.CharField(max_length=100,choices=BUILDING_CHOICES,null=True)
    sub_county = models.CharField(max_length=100, choices=SUB_COUNTY_CHOICES,null=True)
    ward = models.CharField(max_length=100, choices=WARD_CHOICES,null=True)
    floor = models.CharField(max_length=100, choices=FLOOR_CHOICES,null=True)




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

