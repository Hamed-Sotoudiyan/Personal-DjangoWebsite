from django.shortcuts import render
import requests
from django.contrib import messages
from .models import about_detail

# Create your views here.

def main(request):
    context = {
        'about_detail_for_template' : about_detail.objects.last()
    }
    return render (request, 'about/about.html', context)
