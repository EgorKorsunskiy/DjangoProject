# Generated by Django 3.0.3 on 2020-02-21 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200221_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='1111', max_length=36),
        ),
    ]
