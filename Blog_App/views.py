from django.shortcuts import render
from .models import post

# Create your views here.

def home(request):
    context={
        'posts': post.objects.all()


    }
    return render(request, 'Blog_App/home.html',context)

def about(request):
    context={
        'title': 'About'
    }
    return render(request, 'Blog_App/about.html',context)