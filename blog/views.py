from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
    books=Book.objects.all()
    context={
        'books':books
    }
    return render(request, 'index.html',context)

def contact(request):
    return HttpResponse("Bu contact")

def salom(request):
    return HttpResponse("Nima qilyapsan bu yerda adashib ")

def about(request):
    return render(request,'about.html')