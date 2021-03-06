# Generated by Django 3.0.3 on 2020-02-13 15:04

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('rating', models.IntegerField(default=0)),
                ('vip_status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('publication_data', models.DateTimeField()),
                ('user', models.ForeignKey(default='Deleted', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.User')),
            ],
            managers=[
                ('ad', django.db.models.manager.Manager()),
            ],
        ),
    ]
