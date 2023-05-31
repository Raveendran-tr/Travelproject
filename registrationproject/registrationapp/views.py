from django.contrib import messages, auth
from django.shortcuts import render, redirect

from django.contrib.auth.models import User


def index(request):
    return render(request,"index1.html")

