from django.db import models

# Create your models here.


class Team(models.Model):
    image = models.ImageField(upload_to='media/slider/%Y/%m')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=155)
    insta_link = models.CharField(max_length=255)
    ytube_link = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Slider(models.Model):
    photo = models.ImageField(upload_to='media/slider/%Y')
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=200)
    button_text = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline
