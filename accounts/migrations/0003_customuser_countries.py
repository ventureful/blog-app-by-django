# Generated by Django 4.0.7 on 2022-08-12 00:43

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='countries',
            field=django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='Country'),
        ),
    ]
