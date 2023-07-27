from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book

def home(request):
  template = loader.get_template('app.html')
  context = {
    'books': Book.objects.all(),
  }
  return HttpResponse(template.render(context, request))

def book(req, slug):
  return HttpResponse("<h1>Wow!</h1>")



