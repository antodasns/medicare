# Generated by Django 2.2.3 on 2019-11-15 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0009_doctor_details_appoint_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_details',
            name='phone',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor_details',
            name='place',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]