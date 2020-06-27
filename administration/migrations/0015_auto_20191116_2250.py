# Generated by Django 2.2.3 on 2019-11-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0014_auto_20191116_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ref_id', models.CharField(max_length=10)),
                ('doctor_ref_id', models.CharField(max_length=10)),
                ('prescription', models.TextField()),
                ('diets_tips', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='diets_tips',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='prescription',
        ),
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='week_id',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
