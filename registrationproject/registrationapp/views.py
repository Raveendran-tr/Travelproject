from django.contrib import messages, auth
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

def demo(request):
    obj = Places.objects.all()

    return render(request,"index1.html",{'result':obj})
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,"index1.html")
            return redirect("login")

        else:
            messages.info("invalid credentials")

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

            elif User.objects.filter(email=email).exists():
                messages.info(request,"mail exists")

            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                return redirect('login')
                print("user created")


        else:
            messages.info(request,"incorrect password")
    return render(request,"registration.html")
def index(request):
    return render(request,"index1.html")
def logout(request):
    auth.logout(request)
    return render(request,"register.html")