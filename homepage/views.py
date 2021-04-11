from django.http import HttpResponse
from django.shortcuts import render
from .models import Homepage, News, Intro


def index(request):
    homepages = Homepage.objects.all()
    newss = News.objects.all()
    return render(request, 'index.html', {'homepages': homepages, 'newss': newss})


def intro(request):
    homepages = Homepage.objects.all()
    newss = News.objects.all()
    intros = Intro.objects.all()
    return render(request, 'intro.html', {'homepages': homepages, 'newss': newss, 'intros':intros})
    # return render(request, 'intro.html')
    # return HttpResponse("This page is for introduction of BG Group.")


def message(request):
    newss = News.objects.all()
    intros = Intro.objects.all()
    return render(request, 'message.html', {'newss':newss, 'intros':intros})
    # return HttpResponse("This page describes the sevices provided by the BG Group.")


def contact(request):
    newss = News.objects.all()
    intros = Intro.objects.all()
    return render(request, 'contact.html', {'newss':newss, 'intros':intros})
    # return HttpResponse("This is the contact page of BG Group.")

