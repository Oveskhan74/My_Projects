# Generated by Django 5.0.1 on 2024-02-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renty', '0011_alter_property_details_prop_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_details',
            name='prop_img',
            field=models.ImageField(blank=True, null=True, upload_to='property'),
        ),
    ]
