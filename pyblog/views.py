# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello World!! It Pyblog time.")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("This is the about Page.")
    return render(request, 'about.html')