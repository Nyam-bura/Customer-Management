# Generated by Django 5.0.1 on 2024-01-31 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_business_building_name_business_floor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='sub_county',
            field=models.CharField(choices=[('Nairobi', [('Kasarani', 'Kasarani'), ('Westlands', 'Westlands')]), ('Mombasa', [('Nyali', 'Nyali'), ('Likoni', 'Likoni')])], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='ward',
            field=models.CharField(choices=[('Kasarani', [('isipe', 'isipe'), ('Sunton', 'Sunton'), ('hunters', 'hunters')]), ('Westlands', [('Parklands', 'Parklands'), ('Spring Valley', 'Spring Valley')])], max_length=100, null=True),
        ),
    ]