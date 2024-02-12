from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from .models import Business, County

class Command(BaseCommand):
    help = 'Fixes invalid foreign keys in the customer_business table'

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                for business in Business.objects.all():
                    try:
                        county = County.objects.get(county_name=business.county)
                        business.county = county
                        business.save()
                    except County.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f"No matching County found for business: {business.business_name}"))

        except Exception as e:
            raise CommandError(f"An error occurred: {str(e)}")

        self.stdout.write(self.style.SUCCESS('Foreign keys fixed successfully'))
