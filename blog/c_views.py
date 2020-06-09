from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Announcement, PageDetail, Website
from .forms import PostForm, AnnouncementForm, PageDetailForm, WebsiteForm
from django.views.generic import View

def console(request):
    if request.user.is_superuser:
        return render(request, 'console/home.html')
    else:
        return redirect("404")

def newpost(request):
    if request.user.is_superuser:
        objs = Post.objects.all()
        if request.method == 'GET':
            form = PostForm()
            form.fields['author'].initial=request.user  
        else:  # POST
            form = PostForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
            return redirect('newpost')
        return render(request, 'console/newpost.html', {'form': form, 'objs': objs })
    else:
        return redirect("404")

def editpost(request, pk):
    if request.user.is_superuser:
        obj = Post.objects.get(id=pk)
        if request.method == 'GET':
            form = PostForm(instance=obj)
            objs = Post.objects.all()
        else:  # POST
            form = PostForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            return redirect('newpost')
        return render(request, 'console/editpost.html', {'form': form, 'objs': objs })
    else:
        return redirect("404")

def deletepost(request, pk):
    if request.user.is_superuser:
        obj = Post.objects.get(id=pk)
        obj.delete()
        return redirect('newpost')
    else:
        return redirect("404")

def newannouncement(request):
    if request.user.is_superuser:
        objs = Announcement.objects.all()
        if request.method == 'GET':
            form = AnnouncementForm()
            form.fields['author'].initial=request.user  
        else:  # POST
            form = AnnouncementForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('newannouncement')
        return render(request, 'console/newannouncement.html', {'form': form, 'objs': objs })
    else:
        return redirect("404")

def editannouncement(request, pk):
    if request.user.is_superuser:
        obj =Announcement.objects.get(id=pk)
        if request.method == 'GET':
            form = AnnouncementForm(instance=obj)
            objs = Announcement.objects.all()
        else:  # POST
            form = AnnouncementForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            return redirect('newannouncement')
        return render(request, 'console/editannouncement.html', {'form': form, 'objs': objs })
    else:
        return redirect("404")

def deleteannouncement(request, pk):
    if request.user.is_superuser:
        obj = Announcement.objects.get(id=pk)
        obj.delete()
        return redirect('newannouncement')
    else:
        return redirect("404")

def pageedit(request, pk):
    if request.user.is_superuser:
        obj = PageDetail.objects.get(id=pk)
        if request.method == 'GET':
            form = PageDetailForm(instance=obj)
            objs = PageDetail.objects.all()
        else: # POST
            form = PageDetailForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            return redirect('console')
        return render(request, 'console/pages.html', {'form': form, 'objs': objs})
    else:
        return redirect("404")

def websiteedit(request):
    if request.user.is_superuser:
        obj = Website.objects.get(id=1)
        if request.method == 'GET':
            form = WebsiteForm(instance=obj)
        else: # POST
            form = WebsiteForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            return redirect('console')
        return render(request, 'console/website.html', {'form': form})
    else:
        return redirect("404")

def error404(request):
    return render(request, 'console/404.html')