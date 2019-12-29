from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post, Announcement, PageDetail, Website
import datetime
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login,logout


def home(request):
    context={
        'posts': Post.objects.all().exclude(tag='SAMPLE MATERIALS').exclude(tag='ARCHIVES').order_by('-date_posted'),
        'announces': Announcement.objects.all().order_by('-id')[:7],
        'now' : datetime.datetime.now().strftime("%Y"),
        'website': Website.objects.filter(id=1),
       }
    
    return render(request, 'blog/home.html', context)

def pgtrb(request):
    context={
        'posts': Post.objects.filter(tag='PG TRB').order_by('-date_posted'),
        'announces': Announcement.objects.all().order_by('-id')[:7],
        'pages': PageDetail.objects.filter(title='PG TRB'),
        'now' : datetime.datetime.now().strftime("%Y"),
        'website': Website.objects.filter(id=1),
       }
    return render(request, 'blog/pgtrb.html', context)

def ugtrb(request):
    context={
        'posts': Post.objects.filter(tag='UG TRB').order_by('-date_posted'),
        'announces': Announcement.objects.all().order_by('-id')[:7],
        'pages': PageDetail.objects.filter(title='UG TRB'),
        'now' : datetime.datetime.now().strftime("%Y"),
        'website': Website.objects.filter(id=1),
       }
    return render(request, 'blog/ugtrb.html', context)

def polytrb(request):
    context={
        'posts': Post.objects.filter(tag='POLY TRB').order_by('-date_posted'),
        'announces': Announcement.objects.all().order_by('-id')[:7],
        'pages': PageDetail.objects.filter(title='POLY TRB'),
        'now' : datetime.datetime.now().strftime("%Y"),
        'website': Website.objects.filter(id=1),
       }
    return render(request, 'blog/polytrb.html', context)

def enggtrb(request):
    context={
        'posts': Post.objects.filter(tag='ENGG TRB').order_by('-date_posted'),
        'announces': Announcement.objects.all().order_by('-id')[:7],
        'pages': PageDetail.objects.filter(title='ENGG TRB'),
        'now' : datetime.datetime.now().strftime("%Y"),
        'website': Website.objects.filter(id=1),
       }
    return render(request, 'blog/enggtrb.html', context)

def tnset(request):
    context={
        'posts': Post.objects.filter(tag='TNSET').order_by('-date_posted'),
        'announces': Announcement.objects.all().order_by('-id')[:7],
        'pages': PageDetail.objects.filter(title='TNSET'),
        'now' : datetime.datetime.now().strftime("%Y"),
        'website': Website.objects.filter(id=1),
       }
    return render(request, 'blog/tnset.html', context)

def sample(request):
    context={
        'posts': Post.objects.filter(tag='SAMPLE MATERIALS').order_by('-date_posted'),
        'announces': Announcement.objects.all().order_by('-id')[:7],
        'pages': PageDetail.objects.filter(title='SAMPLE'),
        'now' : datetime.datetime.now().strftime("%Y"),
        'website': Website.objects.filter(id=1),
       }
    return render(request, 'blog/sample.html', context)

def archives(request):
    context={
        'posts': Post.objects.filter(tag='ARCHIVES').order_by('-date_posted'),
        'announces': Announcement.objects.all().order_by('-id')[:7],
        'pages': PageDetail.objects.filter(title='ARCHIVES'),
        'now' : datetime.datetime.now().strftime("%Y"),
        'website': Website.objects.filter(id=1),
       }
    return render(request, 'blog/archives.html', context)

def about(request):
    context={
        'announces': Announcement.objects.all().order_by('-id')[:7],
        'website': Website.objects.filter(id=1),
        'now' : datetime.datetime.now().strftime("%Y"),
    }
    return render(request, 'blog/about.html', context)

