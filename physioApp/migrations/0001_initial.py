# Generated by Django 3.1.4 on 2023-04-15 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Praticiene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('praticien_name', models.CharField(max_length=50)),
                ('specialization', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programe_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('feature1', models.CharField(blank=True, max_length=150, null=True)),
                ('feature2', models.CharField(blank=True, max_length=150, null=True)),
                ('feature3', models.CharField(blank=True, max_length=150, null=True)),
                ('feature4', models.CharField(blank=True, max_length=150, null=True)),
                ('feature5', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('testimonial', models.TextField(max_length=350)),
                ('patient_name', models.CharField(blank=True, max_length=50, null=True)),
                ('profession', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]