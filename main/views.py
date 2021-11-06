from django.shortcuts import render , get_list_or_404 , redirect
from .models import Main
from news.models import News

def home(request):

   site = Main.objects.get(pk=1)
   news = News.objects.all()
   context = {
    
    'site':site,
    'news':news,

    }

   return render(request , 'front/home.html',context)

def about(request):

   return render(request , 'front/about.html')

