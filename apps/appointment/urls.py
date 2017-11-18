from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/(?P<id>\d*)$', views.viewAppointment),
    url(r'^addAppointment$', views.addAppointment),
    url(r'^edit/(?P<id>\d*)$', views.editAppointment, name="edit"),
    url(r'^delete/(?P<id>\d*)$', views.deleteAppointment, name="edit")
]