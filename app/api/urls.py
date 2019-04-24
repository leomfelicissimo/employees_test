from django.urls import path
from . import controllers

urlpatterns = [
    path('', controllers.index, name='index')
]