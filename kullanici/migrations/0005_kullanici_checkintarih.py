# Generated by Django 3.0.5 on 2020-05-29 08:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kullanici', '0004_kullanici_checkin'),
    ]

    operations = [
        migrations.AddField(
            model_name='kullanici',
            name='checkinTarih',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), blank=True, null=True, size=None),
        ),
    ]
