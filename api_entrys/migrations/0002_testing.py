# Generated by Django 4.2.5 on 2023-11-14 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_entrys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField()),
            ],
        ),
    ]