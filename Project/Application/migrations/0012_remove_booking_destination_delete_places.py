# Generated by Django 4.2.2 on 2023-07-25 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0011_alter_booking_aadhar_alter_booking_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='destination',
        ),
        migrations.DeleteModel(
            name='Places',
        ),
    ]
