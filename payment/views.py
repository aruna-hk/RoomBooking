from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Mpesa(request):
    return HttpResponse("Mpesa payment")

def Bank(request):
    return HttpResponse("Bank Transfer")

