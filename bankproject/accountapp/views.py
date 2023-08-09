from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from django.contrib import messages, auth

# Create your views here.
def accountopen(request):
    return render(request,"acc.html")
    
def blankfun(request):
    return render(request,"acc.html")

