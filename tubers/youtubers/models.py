from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


class Youtuber(models.Model):

    crew_choices = (
        ('solo', 'solo'),
        ('duet', 'duet'),
        ('team', 'team'),
    )

    camera_choices = (
        ('Canon', 'Canon'),
        ('Nikon', 'Nikon'),
        ('Sony', 'Sony'),
        ('Fuji', 'Fuji'),
        ('DSV', 'DSV'),
        ('SVG', 'SVG'),
    )

    category_choices = (
        ('Featness','Featness'),
        ('comedy', 'comedy'),
        ('moto Vlogs', 'moto Vlogs'),
        ('tech review', 'tech review'),
        ('travel Vlogs', 'travel Vlogs'),
        ('hikeing Vlogs', 'hikeing Vlogs'),
        ('cooking', 'cooking'),
    )

    photo = models.ImageField(upload_to='media/ytuber/%Y/%m')
    fullname = models.CharField(max_length=255)
    price = models.IntegerField()
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choices, max_length=255)
    camera = models.CharField(choices=camera_choices, max_length=255)
    category = models.CharField(choices=category_choices, max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
