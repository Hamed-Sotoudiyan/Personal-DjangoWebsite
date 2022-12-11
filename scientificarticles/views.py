from django.shortcuts import render
import requests
from django.contrib import messages
from .models import Articles

# Create your views here.

def main(request):
    context = {
        'scientificarticles_for_template' : Articles.objects.all()
    }
    return render (request, 'scientificarticles/scientificarticles.html', context)
