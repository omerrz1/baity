# Generated by Django 4.0.6 on 2023-01-31 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_remove_house_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='address',
            field=models.TextField(null=True),
        ),
    ]
