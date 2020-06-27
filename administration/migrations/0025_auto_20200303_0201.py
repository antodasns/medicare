# Generated by Django 2.2.3 on 2020-03-02 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0024_specilizatin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='result',
        ),
        migrations.RemoveField(
            model_name='results',
            name='user_ref_id',
        ),
        migrations.AddField(
            model_name='results',
            name='rating',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='results',
            name='review',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
