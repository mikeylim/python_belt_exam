from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from datetime import datetime

# Create your views here.

def index(request):    
    return render(request,'login/index.html')

def register(request):
    if request.method=="POST":
        user = User.objects.register(request.POST)
        if isinstance(user, list):
            for error in user:
                messages.add_message(request, messages.INFO, error)
            return redirect('/show_register')
        else:
            request.session['name'] = user.first_name
            request.session['user_id'] = user.id
            return redirect('/appointment')
    return redirect('/show_register')

def login(request):
    if request.method=="POST":
        user = User.objects.login(request.POST)
        if isinstance(user, list):
            for error in user:
                messages.add_message(request, messages.INFO, error)
            return redirect('/show_login')
        else:
            request.session['name'] = user.first_name
            request.session['user_id'] = user.id
            return redirect('/appointment')
    return redirect('/show_login')

def logout(request):
    request.session.pop('name')
    request.session.pop('user_id')
    return redirect('/')

def show_login(request):
    return render(request,'login/login.html')

def show_register(request):
    return render(request,'login/register.html')