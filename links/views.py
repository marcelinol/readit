# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

def index(request):
    articles_list = Article.objects.all()
    template = loader.get_template('links/index.html')
    context= {
        'articles_list': articles_list,
    }
    return HttpResponse(template.render(context, request))
