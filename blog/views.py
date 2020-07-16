from django.shortcuts import render
from .models import Blogpost
from django.http import HttpResponse
# Create your views here.

def index(request):
    posts = Blogpost.objects.all()
    return render(request,'blog/index.html',{'posts':posts})

def blogPost(request , id ):
    posts = Blogpost.objects.filter(post_id  = id)[0]
    return render(request,'blog/blogpost.html',{'posts':posts})