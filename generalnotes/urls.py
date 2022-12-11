from django.urls import path
from . import views

app_name = 'generalnotes'

urlpatterns = [
    path('', views.main, name='main'),
]
