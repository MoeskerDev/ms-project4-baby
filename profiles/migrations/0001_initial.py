"""
Migration of the profile app
"""
# Generated by Django 3.2.7 on 2021-10-26 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):
    """
    Migration of profile app containing three
    models; UserProfile, WishList and Review
    """
    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('default_phone_number', models.CharField(blank=True,
                 max_length=20, null=True)),
                ('default_street_address1', models.CharField(blank=True,
                 max_length=80, null=True)),
                ('default_street_address2', models.CharField(blank=True,
                 max_length=80, null=True)),
                ('default_town_or_city', models.CharField(blank=True,
                 max_length=40, null=True)),
                ('default_county', models.CharField(blank=True,
                 max_length=80, null=True)),
                ('default_postcode', models.CharField(blank=True,
                 max_length=20, null=True)),
                ('default_country', django_countries.fields.CountryField(
                    blank=True, max_length=2, null=True)),
                ('user',
                 models.OneToOneField(
                     on_delete=django.db.models.deletion.CASCADE,
                     to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(blank=True, null=True,
                                              on_delete=django.db.
                                              models.deletion.CASCADE,
                                              to='products.product')),
                ('user', models.ForeignKey(blank=True, null=True,
                                           on_delete=django.db.
                                           models.deletion.CASCADE,
                                           to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2,
                 default=0, max_digits=6)),
                ('review', models.TextField(null=True)),
                ('product', models.ForeignKey(blank=True, null=True,
                                              on_delete=django.db.
                                              models.deletion.CASCADE,
                                              to='products.product')),
                ('user', models.ForeignKey(blank=True, null=True,
                                           on_delete=django.db.
                                           models.deletion.CASCADE,
                                           to='profiles.userprofile')),
            ],
        ),
    ]
