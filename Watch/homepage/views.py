from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse("Welcome to Home page")
def About(request):
    return HttpResponse("About Page")

