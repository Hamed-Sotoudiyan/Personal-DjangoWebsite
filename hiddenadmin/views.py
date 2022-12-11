from django.shortcuts import render,redirect
import requests
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from contact.models import Contact
from about.models import about_detail
from applypeyma.models import ApplyPeyma
from translations.models import Translations
from scientificarticles.models import Articles
from generalnotes.models import GeneralNotes
from business.models import Business,Images
from home.models import Home

# Create your views here.

def authentication(request):
    if request.method == 'POST':
        user = authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            login(request,user)
            return redirect('hiddenadmin:adminpagemenu')
    return render (request, 'hiddenadmin/authentication.html')

def adminpagemenu(request):
    if request.method == 'POST':
        logout(request)
        return redirect('hiddenadmin:authentication')
    return render(request, 'hiddenadmin/adminpagemenu.html')

def recievedmessages(request):
    if (request.method == 'POST' and 'deleteBtn' in request.POST and len(request.POST.get('RMid')) !=0):
        Contact.objects.filter(id=int(request.POST.get('RMid'))).delete()
    context = {
        'recieved_contacts_for_template' : Contact.objects.all()
    }
    return render(request,'hiddenadmin/recievedmessages.html',context)

def adminabout(request):
    if request.method == 'POST':
        if ('title1btn' in request.POST and len(request.POST.get('title1')) !=0):
            about_detail.objects.filter(id=1).update(title1=request.POST.get('title1'))
        elif ('title2btn' in request.POST and len(request.POST.get('title2')) !=0):
            about_detail.objects.filter(id=1).update(title2=request.POST.get('title2'))
        elif ('imagebtn' in request.POST and ( 'image' in request.FILES)):
            obj = about_detail.objects.last()
            obj.image = request.FILES['image']
            obj.save()
        elif ('resumebtn' in request.POST and ( 'resume' in request.FILES)):
            obj = about_detail.objects.last()
            obj.resume = request.FILES['resume']
            obj.save()
        context = {
            'about_detail_for_template' : about_detail.objects.last()
        }
    else :
        context = {
            'about_detail_for_template' : about_detail.objects.last()
        }
    return render(request,'hiddenadmin/adminabout.html',context)

def applypeyma(request):
    if request.method == 'POST':
        if ('text1btn' in request.POST and len(request.POST.get('text1')) !=0):
            ApplyPeyma.objects.filter(id=1).update(text1=request.POST.get('text1'))
        elif ('text2btn' in request.POST and len(request.POST.get('text2')) !=0):
            ApplyPeyma.objects.filter(id=1).update(text2=request.POST.get('text2'))
        context = {
            'applypeyma_for_template' : ApplyPeyma.objects.last()
        }
    else :
        context = {
            'applypeyma_for_template' : ApplyPeyma.objects.last()
        }
    return render(request,'hiddenadmin/adminapplypeyma.html',context)

def translations(request):
    if request.method == 'POST':
        if ('savebtn' in request.POST and len(request.POST.get('titlesave')) !=0
            and len(request.POST.get('textsave')) !=0
            and ( 'articlesave' in request.FILES)):

            TranslationsFormData = Translations(title=request.POST.get('titlesave'),
                                          text=request.POST.get('textsave'),
                                          article=request.FILES['articlesave'])
            TranslationsFormData.save()
        elif ('deleteBtn' in request.POST and len(request.POST.get('Tid')) !=0) :
            Translations.objects.filter(id=int(request.POST.get('Tid'))).delete()

    context = {
        'translations_for_template' : Translations.objects.all()
    }
    return render(request,'hiddenadmin/admintranslations.html',context)

def scientificarticles(request):
    if request.method == 'POST':
        if ('savebtn' in request.POST and len(request.POST.get('titlesave')) !=0
            and len(request.POST.get('textsave')) !=0
            and ( 'articlesave' in request.FILES)):

            ArticlesFormData = Articles(title=request.POST.get('titlesave'),
                                          text=request.POST.get('textsave'),
                                          article=request.FILES['articlesave'])
            ArticlesFormData.save()
        elif ('deleteBtn' in request.POST and len(request.POST.get('SAid')) !=0) :
            Articles.objects.filter(id=int(request.POST.get('SAid'))).delete()

    context = {
        'Articles_for_template' : Articles.objects.all()
    }
    return render(request,'hiddenadmin/adminscientificarticles.html',context)

def generalnotes(request):
    if request.method == 'POST':
        if ('savebtn' in request.POST and len(request.POST.get('titlesave')) !=0
            and len(request.POST.get('textsave')) !=0
            and len(request.POST.get('datesave')) !=0
            and len(request.POST.get('authersave')) !=0
            and len(request.POST.get('typesave')) !=0
            and ( 'articlesave' in request.FILES)):

            GeneralNotesFormData = GeneralNotes(title=request.POST.get('titlesave'),
                                          text=request.POST.get('textsave'),
                                          date=request.POST.get('datesave'),
                                          type=request.POST.get('typesave'),
                                          auther=request.POST.get('authersave'),
                                          article=request.FILES['articlesave'])
            GeneralNotesFormData.save()
        elif ('deleteBtn' in request.POST and len(request.POST.get('GNid')) !=0) :
            GeneralNotes.objects.filter(id=int(request.POST.get('GNid'))).delete()

    context = {
        'GeneralNotes_for_template' : GeneralNotes.objects.all()
    }
    return render(request,'hiddenadmin/admingeneralnotes.html',context)

def business(request):
    if request.method == 'POST':
        if ('savebtn' in request.POST and len(request.POST.get('titlesave')) !=0
            and len(request.POST.get('textsave')) !=0
            and len(request.POST.get('datesave')) !=0
            and len(request.POST.get('related_urlsave')) !=0
            and len(request.POST.get('typesave')) !=0
            and ( 'image_one' in request.FILES)):

            BusinessFormData = Business(title=request.POST.get('titlesave'),
                                          text=request.POST.get('textsave'),
                                          date=request.POST.get('datesave'),
                                          type=request.POST.get('typesave'),
                                          related_url=request.POST.get('related_urlsave'),
                                          image=request.FILES['image_one'])
            BusinessFormData.save()

            if ('image_two' in request.FILES) :
                last_id = Business.objects.last()
                ImageBusinessFormData = Images(image=request.FILES['image_two'],
                                               business_id=last_id)
                ImageBusinessFormData.save()
            if ('image_three' in request.FILES) :
                last_id = Business.objects.last()
                ImageBusinessFormData = Images(image=request.FILES['image_three'],
                                               business_id=last_id)
                ImageBusinessFormData.save()
            if ('image_four' in request.FILES) :
                last_id = Business.objects.last()
                ImageBusinessFormData = Images(image=request.FILES['image_four'],
                                               business_id=last_id)
                ImageBusinessFormData.save()
        elif ('deleteBtn' in request.POST and len(request.POST.get('Bid')) !=0) :
            Business.objects.filter(id=int(request.POST.get('Bid'))).delete()

    context = {
        'business_for_template' : Business.objects.all()
    }
    return render (request,'hiddenadmin/adminbusiness.html',context)

def home(request):
    if request.method == 'POST':
        if ('titlebtn' in request.POST and len(request.POST.get('title')) !=0):
            Home.objects.filter(id=1).update(title=request.POST.get('title'))
        elif ('textbtn' in request.POST and len(request.POST.get('text')) !=0):
            Home.objects.filter(id=1).update(text=request.POST.get('text'))
        elif ('image_onebtn' in request.POST and ( 'image_one' in request.FILES)):
            obj = Home.objects.last()
            obj.image_one = request.FILES['image_one']
            obj.save()
        elif ('image_twobtn' in request.POST and ( 'image_two' in request.FILES)):
            obj = Home.objects.last()
            obj.image_two = request.FILES['image_two']
            obj.save()
        elif ('image_threebtn' in request.POST and ( 'image_three' in request.FILES)):
            obj = Home.objects.last()
            obj.image_three = request.FILES['image_three']
            obj.save()
        elif ('image_fourbtn' in request.POST and ( 'image_four' in request.FILES)):
            obj = Home.objects.last()
            obj.image_four = request.FILES['image_four']
            obj.save()
        context = {
            'home_for_template' : Home.objects.last()
        }
    else :
        context = {
            'home_for_template' : Home.objects.last()
        }
    return render(request,'hiddenadmin/adminhome.html',context)
