from django.db import models

# Create your models here.


class Home (models.Model):
    title = models.TextField(blank=False)
    text = models.TextField(blank=False)
    image_one = models.ImageField(upload_to='home',blank=True)
    image_two = models.ImageField(upload_to='home',blank=True)
    image_three = models.ImageField(upload_to='home',blank=True)
    image_four = models.ImageField(upload_to='home',blank=True)

    def __str__ (self):
        return self.title
