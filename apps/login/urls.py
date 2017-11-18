from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),    
    url(r'^logout$', views.logout),
    url(r'^register$', views.register),
    url(r'^show_login$', views.show_login),
    url(r'^show_register$', views.show_register),
]