from django.db import models

# Create your models here.

class Translations (models.Model):
    title = models.TextField(blank=False)
    text = models.TextField(blank=False)
    article = models.FileField(upload_to='translations')

    def __str__ (self):
        return self.title
