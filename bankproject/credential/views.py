
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.

def logfun(request):
    if request.method=='POST':
        user_name=request.POST['username']
        pass_word=request.POST['password']
        user=auth.authenticate(username=user_name,password=pass_word)

        if user is not None:
            auth.login(request,user)
            return render(request,"blank.html")
        else:
            messages.info(request,"invalid credentials")
            return redirect('credential:logfun')
             
    return render(request,"login.html") 



def regfun(request):
    if request.method=='POST':      
        user_name=request.POST['username']  
        first_name=request.POST['first_name']
        l_name=request.POST['last_name']
        email=request.POST['email']
        pword=request.POST['password']
        cpword=request.POST['password']
        gender = request.POST['gender']
        country = request.POST['country']
    
        if pword==cpword:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username already Exists")
                return redirect('credential:regfun')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('credential:regfun')
            else:
                user=User.objects.create_user(username=user_name,password=pword,first_name=first_name,last_name=l_name,email=email)
                user.save();
                return redirect('credential:logfun')
            
        else:
            messages.info(request,"Password not matching!!")
            return redirect('credential:regfun')
      
    return render(request,"registration.html") 

def logoutfun(request):
    auth.logout(request)
    return redirect('/')