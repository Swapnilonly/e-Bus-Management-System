# Generated by Django 5.1.4 on 2025-01-08 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_postbuscontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostBusType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bustype', models.CharField(max_length=10)),
                ('buscapacity', models.CharField(max_length=10)),
                ('buscdescription', models.CharField(max_length=50)),
            ],
        ),
    ]
