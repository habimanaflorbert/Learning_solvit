#python
import os

#django
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse 
from django.contrib.auth.decorators import login_required

#third_parts

#models
from blog.models import Author, News
from blog.forms import BookForm, Myforms,NewsForm
from blog.decorators import staff_required,has_authenticated_user
#

# Create your views here.

def home(request):
    news=News.objects.last()
    context={'news':news,'title':'News for today'}
    return render(request,'index.html',context)


def details(request,id):
    news=News.objects.get(id=id)
    context={'news':news,'title':'News for today'}
    return render(request,'blog/details.html',context)

def my_blogs(request):
    news=News.objects.all()
    context={'news':news,'title':'News for today'}
    return render(request,'blog/list_blog.html',context)

@has_authenticated_user()
@staff_required()
def add_news(request):
    request.session.clear()
    authors=Author.objects.all()
    forms=BookForm()
    if request.method=='POST':
        forms=BookForm(request.POST)
        if forms.is_valid():
           forms.save()
           return redirect('home')
        else:
           
            context={'forms':forms,'authors':authors}
            return render(request, 'blog/add_news.html',context)


           
    context={'authors':authors,'forms':forms}
    return render(request, 'blog/add_news.html',context)

class MyView(View):
    def get(self,request):
        return HttpResponse("get body")

    def post(self,request):
        return HttpResponse("post body")