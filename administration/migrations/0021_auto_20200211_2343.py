# Generated by Django 2.2.3 on 2020-02-11 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0020_auto_20200114_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='address',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_details',
            name='age',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_details',
            name='bloodgroup',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_details',
            name='gender',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_details',
            name='phone',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]