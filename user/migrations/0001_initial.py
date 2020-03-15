# Generated by Django 3.0.3 on 2020-02-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('rating', models.IntegerField(default=0)),
                ('vip_status', models.BooleanField()),
            ],
        ),
    ]
