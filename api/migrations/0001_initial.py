# Generated by Django 4.2.4 on 2023-09-16 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_event_start', models.DateTimeField()),
                ('event_name', models.CharField(max_length=200)),
                ('name_event_image', models.CharField(max_length=200)),
                ('event_image', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=400)),
                ('protocols', models.CharField(max_length=500)),
                ('capacity', models.IntegerField()),
                ('entry_price', models.FloatField()),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
