from django.shortcuts import render , get_list_or_404 , redirect
from .models import News

def new_detail(request,new_id):

    new_detail = News.objects.filter(pk=new_id)
    
    context = {
     'new_detail':new_detail,
    }
    return render(request, 'front/new_detail.html', context)
