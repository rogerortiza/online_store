# Generated by Django 3.0.8 on 2020-07-24 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coupons',
            new_name='Coupon',
        ),
    ]