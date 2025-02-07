from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Assalomu alaykum !!!")

def contact(request):
    return HttpResponse("Bu contact")