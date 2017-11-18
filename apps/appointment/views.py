# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Appointment, User
from django.contrib import messages
import datetime

# Create your views here.
def index(request):
    context = { 'appointments' : Appointment.objects.getAppointment(request.session['user_id']), 
                'current_time' : datetime.datetime.today().strftime('%b %d %Y'),
                }
    # request.session['current_time'] = datetime.date.today()
    return render(request,'appointment/index.html', context)

def viewAppointment(request, id):    
    context = {'appointment' : Appointment.objects.get(id=id)}
    return render(request,'appointment/index.html')

def addAppointment(request):    
    if request.method == "POST":
        postData = { 'user': request.session['user_id'],
                     'appointment': request.POST['appointment'],
                     'time': request.POST['time'],
                     'status': 'pending',
                     'date': request.POST['date'] }
        appointment = Appointment.objects.addAppointment(postData)
        if not isinstance(appointment, Appointment):
            messages.add_message(request, messages.ERROR, appointment)
            return redirect('appointment/addAppointment')       
        return redirect('/appointment')
    elif request.method == "GET":        
        context = { 'appointment': Appointment.objects.all() } 
        return render(request, 'book_reviews/add.html', context)     

def editAppointment(request, id):    
    return render(request,'appointment/edit.html')

def deleteAppointment(request, id):    
    if request.method == "GET":
        context = { 'appointment': Appointment.objects.get(id=id) }
        if request.session['user_id'] != context['appointment'].user.id:
            request.session["wrong_id"] = "Oops, users don't match."
        else:
            return render(request, 'appointment/delete.html', context)
    elif request.method == 'POST':
        Appointment.objects.get(id=id).delete()
        return redirect('/appointment')
    
    return redirect('/appointment')
