# Generated by Django 3.2.5 on 2021-07-08 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210708_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestseller',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
