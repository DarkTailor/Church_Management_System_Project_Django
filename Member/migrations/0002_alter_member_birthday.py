# Generated by Django 4.2.6 on 2023-11-19 00:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now, max_length=255),
        ),
    ]
