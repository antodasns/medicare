# Generated by Django 2.2.3 on 2020-01-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0019_auto_20191118_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_details',
            name='approval',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_details',
            name='approval',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]