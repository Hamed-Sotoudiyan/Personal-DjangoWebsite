from django.db import models

# Create your models here.

class about_detail (models.Model):
    title1 = models.TextField(blank=False)
    title2 = models.TextField(blank=False)
    image = models.ImageField(upload_to='about')
    resume = models.FileField(upload_to='about')

    def __str__ (self):
        return self.title1
