from django.db import models

# Create your models here.

class Articles (models.Model):
    title = models.TextField(blank=False)
    text = models.TextField(blank=False)
    article = models.FileField(upload_to='scientificarticles')

    def __str__ (self):
        return self.title
