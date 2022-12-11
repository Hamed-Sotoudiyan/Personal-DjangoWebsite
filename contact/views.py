from django.shortcuts import render
import requests
from django.contrib import messages
from .models import Contact
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def main(request):
    if request.method == 'POST':
        if( len(request.POST.get('name')) !=0 and len(request.POST.get('message')) !=0):
            ContactFormData = Contact(fullname=request.POST.get('name'),
                                          email=request.POST.get('email'),
                                          subject=request.POST.get('subject'),
                                          message=request.POST.get('message'))
            ContactFormData.save()
            messages.success(request, 'Your message has been successfully sent.')
        else:
            messages.error(request,'Please complete the relevant fields!' )
    return render (request, 'contact/contact.html')
