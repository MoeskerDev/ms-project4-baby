# Generated by Django 3.2.7 on 2021-10-22 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_review'),
        ('profiles', '0007_auto_20211019_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
    ]
