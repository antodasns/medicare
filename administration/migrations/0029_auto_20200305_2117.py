# Generated by Django 2.2.3 on 2020-03-05 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0028_payment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='payment',
            new_name='payments',
        ),
    ]