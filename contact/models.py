from django.db import models

# Create your models here.

class Contact (models.Model):
    fullname = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=30, blank=True)
    message = models.TextField(blank=False)

    def __str__ (self):
        return self.fullname
