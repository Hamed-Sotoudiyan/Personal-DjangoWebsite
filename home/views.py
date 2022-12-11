from django.shortcuts import render
import requests
from django.contrib import messages
from translations.models import Translations
from scientificarticles.models import Articles
from generalnotes.models import GeneralNotes
from business.models import Business
from .models import Home

# Create your views here.

def main(request):
    context = {
        'home_for_template' : Home.objects.last(),
        'translations_for_template' : Translations.objects.last(),
        'Articles_for_template' : Articles.objects.last(),
        'GeneralNotes_for_template' : GeneralNotes.objects.last(),
        'business_for_template' : Business.objects.last(),
    }
    return render (request, 'home/home.html',context)
