# Generated by Django 3.0 on 2023-04-26 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('physioApp', '0002_auto_20230425_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
