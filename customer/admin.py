from django.contrib import admin
from customer.models import Customer,Business,County,SubCounty,Ward,BusinessCategories

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

class CountyAdmin(admin.ModelAdmin):
    model = County
    list_display = ['id','county_name']
admin.site.register(County,CountyAdmin)

class SubCountyAdmin(admin.ModelAdmin):
    model = SubCounty
    list_display = ['id','subcounty_name']
admin.site.register(SubCounty,SubCountyAdmin)


class WardAdmin(admin.ModelAdmin):
    model = Ward
    list_display = ['id','ward_name']
admin.site.register(Ward,WardAdmin)

class BusinessCategoriesAdmin(admin.ModelAdmin):
    model = BusinessCategories
    list_display = ['id','title']
admin.site.register(BusinessCategories,BusinessCategoriesAdmin)
