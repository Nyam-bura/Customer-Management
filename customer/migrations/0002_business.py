# Generated by Django 5.0.1 on 2024-01-29 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('business_categories', models.CharField(max_length=100)),
                ('business_registration_date', models.DateField()),
                ('age_of_business', models.DateField()),
            ],
        ),
    ]
