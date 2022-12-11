from django.shortcuts import render
import requests
from django.contrib import messages
from .models import Business,Images

# Create your views here.

def main(request):
    context = {
        'business_for_template' : Business.objects.all()
    }
    return render (request, 'business/business.html',context)

def detail(request,pk):
    context = {
        'business_for_detail_template' : Business.objects.filter(id=int(pk)),
        'business_images_for_detail_template' : Images.objects.filter(business_id=pk)
    }
    return render (request, 'business/business_detail.html',context)
