from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def product_view(request):
    return HttpResponse('Super good')

def home_page(request):
    return HttpResponse('Welcome to the Shop')