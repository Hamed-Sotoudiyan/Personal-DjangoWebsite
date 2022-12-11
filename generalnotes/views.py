from django.shortcuts import render
import requests
from django.contrib import messages
from .models import GeneralNotes

# Create your views here.

def main(request):
    context = {
        'GeneralNotes_for_templates' : GeneralNotes.objects.all()
    }
    return render (request, 'generalnotes/generalnotes.html',context)
