
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.
def bankfun(request):
    obj = User.objects.all()
    return render(request,"index.html",{'obj':obj})

def dropfun(request):
    return render(request,"drop.html")