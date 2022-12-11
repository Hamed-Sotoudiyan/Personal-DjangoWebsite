from django.db import models

# Create your models here.

class Business (models.Model):
    date = models.CharField(max_length=50, blank=False)
    title = models.TextField(blank=False)
    related_url = models.TextField(blank=False)
    type = models.CharField(max_length=50, blank=False)
    text = models.TextField(blank=False)
    image = models.ImageField(upload_to='business', blank=False, null=True)

    def __str__ (self):
        return self.title

class Images (models.Model):
    image = models.ImageField(upload_to='business',blank=True)
    business_id = models.ForeignKey(Business,on_delete=models.CASCADE)
