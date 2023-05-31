from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.shortcuts import render, redirect

from django.contrib.auth.models import User


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,"login.html")







# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']


        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect("registration")

            elif User.objects.filter(email=email).exists():
                messages.info(request,"mail exists")
                return redirect("registration")

            else:

                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                return redirect('login')
                print("user created")


        else:
            messages.info(request,"incorrect password")
            return redirect("registration")
        return redirect('')
    else:
        return render(request,"registration.html")


def logout(request):
    auth.logout(request)
    return redirect('/')



def about(request):
    return render(request,"about.html")
