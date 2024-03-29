# Generated by Django 5.0.1 on 2024-02-12 10:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('county_name', models.CharField(max_length=100, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100, verbose_name='customer_name')),
                ('id_number', models.CharField(max_length=20, unique=True, verbose_name='id_number')),
                ('contact_phone', models.CharField(max_length=20, verbose_name='contact_phone')),
                ('contact_email', models.EmailField(max_length=254, unique=True, verbose_name='contact_email')),
                ('date_of_birth', models.DateField(verbose_name='date_of_birth')),
                ('nationality', models.CharField(choices=[('kenyan', 'kenyan'), ('ugandan', 'ugandan'), ('tanzanian', 'tanzanian'), ('rwandees', 'rwandees')], max_length=50, null=True, verbose_name='nationality')),
            ],
        ),
        migrations.CreateModel(
            name='SubCounty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('subcounty_name', models.CharField(choices=[('WE', 'Westlands'), ('EM', 'Embakasi'), ('DA', 'Dagoretti'), ('CH', 'Changamwe'), ('NY', 'Nyali')], max_length=100, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('ward_name', models.CharField(choices=[('PA', 'Parklands'), ('RI', 'Riruta'), ('KI', 'Kilimani'), ('AI', 'Airport'), ('MK', 'Mkomani')], max_length=100, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100, verbose_name='business_name')),
                ('business_category', models.PositiveSmallIntegerField(choices=[('LA', 'LargeScale'), ('SM', 'SmallScale'), ('WH', 'Wholesale'), ('GR', 'GreenKiosk'), ('RE', 'Retail')], verbose_name='business_category')),
                ('business_registration_date', models.DateField(verbose_name='business_registration')),
                ('building_name', models.CharField(max_length=100, null=True)),
                ('floor', models.PositiveSmallIntegerField(null=True)),
                ('county', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='customer.county')),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='customer.customer', verbose_name='customer')),
                ('sub_county', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.subcounty')),
                ('ward', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.ward')),
            ],
        ),
    ]
