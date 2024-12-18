# Generated by Django 4.2 on 2024-12-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250)),
                ('media', models.ImageField(upload_to='about-us/media/')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'about us',
                'verbose_name_plural': 'about us',
            },
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image_uz', models.ImageField(upload_to='advertisement/image_uz/')),
                ('image_ru', models.ImageField(upload_to='advertisement/image_ru/')),
            ],
            options={
                'verbose_name': 'advertisement',
                'verbose_name_plural': 'advertisements',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image_uz', models.ImageField(upload_to='banner/image_uz/')),
                ('image_ru', models.ImageField(upload_to='banner/image_ru/')),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'banners',
            },
        ),
    ]
