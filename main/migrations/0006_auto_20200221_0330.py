# Generated by Django 3.0.3 on 2020-02-21 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200216_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=models.CharField(max_length=50), max_length=36),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(null=True, upload_to='./ad/templates/ad/'),
        ),
    ]
