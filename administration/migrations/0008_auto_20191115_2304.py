# Generated by Django 2.2.3 on 2019-11-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0007_auto_20191115_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_details',
            name='consolt_fee',
            field=models.CharField(max_length=20),
        ),
    ]
