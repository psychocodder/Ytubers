# Generated by Django 3.1.7 on 2021-02-22 08:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera',
            field=models.CharField(choices=[('Canon', 'Canon'), ('Nikon', 'Nikon'), ('Sony', 'Sony'), ('Fuji', 'Fuji'), ('DSV', 'DSV'), ('SVG', 'SVG')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('comedy', 'comedy'), ('moto Vlogs', 'moto Vlogs'), ('tech review', 'tech review'), ('travel Vlogs', 'travel Vlogs'), ('hikeing Vlogs', 'hikeing Vlogs'), ('cooking', 'cooking')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('duet', 'duet'), ('team', 'team')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
