# Generated by Django 5.0.2 on 2024-03-14 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renty', '0022_property_details_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property_details',
            old_name='prop_img',
            new_name='prop_img1',
        ),
        migrations.AddField(
            model_name='property_details',
            name='prop_img2',
            field=models.ImageField(blank=True, null=True, upload_to='property'),
        ),
        migrations.AddField(
            model_name='property_details',
            name='prop_img3',
            field=models.ImageField(blank=True, null=True, upload_to='property'),
        ),
        migrations.AddField(
            model_name='property_details',
            name='prop_img4',
            field=models.ImageField(blank=True, null=True, upload_to='property'),
        ),
    ]
