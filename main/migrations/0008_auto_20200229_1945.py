# Generated by Django 3.0.3 on 2020-02-29 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200221_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='vip_status',
            field=models.BooleanField(default=False),
        ),
    ]
