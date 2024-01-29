from django.contrib import admin

from customer.models import Customer,Business

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ['customer_name','contact_phone','contact_email','date_of_birth','nationality']
admin.site.register(Customer, CustomerAdmin)

class BusinessAdmin(admin.ModelAdmin):
    model = Business
    list_display = ['business_name','business_categories','business_registration_date','age_of_business']
admin.site.register(Business,BusinessAdmin)
