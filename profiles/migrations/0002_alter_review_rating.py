"""
Latest migration in the profile app
"""
# Generated by Django 3.2.7 on 2021-11-18 17:20

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Adaptation of the review field in the review model
    """
    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]