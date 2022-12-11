from django.urls import path
from . import views

app_name = 'hiddenadmin'

urlpatterns = [
    path('', views.authentication, name='authentication'),
    path('menu/', views.adminpagemenu, name='adminpagemenu'),
    path('recievedmessages/', views.recievedmessages, name='recievedmessages'),
    path('about/', views.adminabout, name='adminabout'),
    path('applypeyma/', views.applypeyma, name='applypeyma'),
    path('translations/', views.translations, name='translations'),
    path('scientificarticles/', views.scientificarticles, name='scientificarticles'),
    path('generalnotes/', views.generalnotes, name='generalnotes'),
    path('business/', views.business, name='business'),
    path('home/', views.home, name='home'),
]
