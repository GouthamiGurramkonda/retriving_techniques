from django.shortcuts import render
from django.db.models.functions import Length

# Create your views here.
from app.models import *

def display_topics(request):
    LOT=Topic.objects.all()
    d={'name':LOT}
    return render(request,'display_topics.html',d)

def webpage(request):
    WOT=Webpage.objects.all()
    WOT=Webpage.objects.filter(name='Rock')
    WOT=Webpage.objects.exclude(topic_name='cricket')
    WOT=Webpage.objects.all()[1:2:]

    WOT=Webpage.objects.all().order_by('name')
    WOT=Webpage.objects.all().order_by('-name')

    WOT=Webpage.objects.all().order_by(Length('name'))
    WOT=Webpage.objects.all().order_by(Length('name').desc())
    d={'name':WOT}
    return render(request,'webpage.html',d)

def accessrecords(request):
    AOT=AccessRecord.objects.all()
    AOT=AccessRecord.objects.filter(author='A')
    AOT=AccessRecord.objects.filter(date__gt='2023-04-02')
    AOT=AccessRecord.objects.filter(date__gte='2023-04-02')
    AOT=AccessRecord.objects.filter(date__lt='2023-04-04')
    AOT=AccessRecord.objects.filter(date__lte='2023-04-04')
    d={'name':AOT}
    return render(request,'accessrecords.html',d)
