# Generated by Django 2.2.3 on 2019-11-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0006_auto_20191115_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_details',
            name='active_days',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor_details',
            name='consolt_fee',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
