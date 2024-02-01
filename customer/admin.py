from django.contrib import admin
from customer.models import Customer,Business,BusinessCategories

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ['customer_name','id_number','contact_phone','contact_email','date_of_birth','nationality']
admin.site.register(Customer, CustomerAdmin)

class BusinessAdmin(admin.ModelAdmin):
    model = Business
    list_display = ['business_name','id','business_registration_date','age_of_business']
    
    def age_of_business(self,obj):
        return obj.age_of_business
    age_of_business.short_description='Age'

admin.site.register(Business,BusinessAdmin)

class BusinessCategoriesAdmin(admin.ModelAdmin):
    model = BusinessCategories
    list_display = ['id','title']
admin.site.register(BusinessCategories,BusinessCategoriesAdmin)
