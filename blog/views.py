from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def index_2(request):
    return render(request,'single.html')