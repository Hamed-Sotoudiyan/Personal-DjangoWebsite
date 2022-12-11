from django.urls import path
from . import views

app_name = 'translations'

urlpatterns = [
    path('', views.main, name='main'),
]
