# Generated by Django 3.0.5 on 2020-05-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kullanici', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kullanici',
            name='userName',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
