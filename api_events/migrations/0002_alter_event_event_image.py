# Generated by Django 4.2.5 on 2023-11-14 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]