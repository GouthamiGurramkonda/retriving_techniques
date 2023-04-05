from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topics(request):
    LOT=Topic.objects.all()
    d={'name':LOT}
    return render(request,'display_topics.html',d)

def webpage(request):
    WOT=Webpage.objects.all()
    d={'name':WOT}
    return render(request,'webpage.html',d)

def accessrecords(request):
    AOT=AccessRecord.objects.all()
    d={'name':AOT}
    return render(request,'accessrecords.html',d)
