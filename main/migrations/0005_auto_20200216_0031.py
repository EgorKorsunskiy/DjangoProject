# Generated by Django 3.0.3 on 2020-02-15 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_ad_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
