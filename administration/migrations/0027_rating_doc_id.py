# Generated by Django 2.2.3 on 2020-03-02 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0026_auto_20200303_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='doc_id',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]