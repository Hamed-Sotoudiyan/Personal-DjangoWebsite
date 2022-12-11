from django.db import models

# Create your models here.

class GeneralNotes (models.Model):
    date = models.CharField(max_length=50, blank=False)
    title = models.TextField(blank=False)
    auther = models.CharField(max_length=50)
    type = models.CharField(max_length=50, blank=False)
    text = models.TextField(blank=False)
    article = models.FileField(upload_to='generalnotes')

    def __str__ (self):
        return self.title
