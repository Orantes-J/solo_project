from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def index(request):
    return HttpResponse('Hello Juan')