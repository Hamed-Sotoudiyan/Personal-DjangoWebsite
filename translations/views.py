from django.shortcuts import render
import requests
from django.contrib import messages
from .models import Translations

# Create your views here.

def main(request):
    context = {
        'Translations_for_template' : Translations.objects.all()
    }
    return render (request, 'translations/translations.html',context)
