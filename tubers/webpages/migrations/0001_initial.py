# Generated by Django 3.1.6 on 2021-02-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/slider/%Y')),
                ('headline', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('button_text', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
