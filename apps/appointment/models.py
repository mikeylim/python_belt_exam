# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from ..login.models import User
import datetime

# Create your models here.
class AppointmentManager(models.Manager):    

    def addAppointment(self, postData):
        user = User.objects.get(id=postData['user'])
        # appointment = Appointment.objects.get(id=postData['appointment_id'])
        try:
            existing_appointment = Appointment.objects.get(appointment=postData['appointment'])
            warning = "The same appointment already exists"
            return warning
        except:            
            return Appointment.objects.create(appointment=postData['appointment'],user=user,status=postData['status'], date=postData['date'], time=postData['time'])

    def getSortedAppointment(self):
        return Appointment.objects.order_by('time')

    def getAppointment(self, user_id):
        return Appointment.objects.filter(user=User.objects.get(id=user_id))


class Appointment(models.Model):
    appointment = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    date = models.DateTimeField()
    time = models.TimeField()
    user = models.ForeignKey(User, related_name="appointments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AppointmentManager()