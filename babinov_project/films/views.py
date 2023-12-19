from django.shortcuts import render
from . import models

def home(request):
    render(models, context='home')
