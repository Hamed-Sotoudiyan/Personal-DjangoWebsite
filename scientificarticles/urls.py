from django.urls import path
from . import views

app_name = 'scientificarticles'

urlpatterns = [
    path('', views.main, name='main'),
]
