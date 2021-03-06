# Generated by Django 2.2.3 on 2020-03-02 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0025_auto_20200303_0201'),
    ]

    operations = [
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=15)),
                ('review', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='results',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='results',
            name='review',
        ),
        migrations.AddField(
            model_name='results',
            name='result',
            field=models.ImageField(default=1, upload_to='result'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='results',
            name='user_ref_id',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
