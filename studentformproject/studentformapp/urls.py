from django.conf.urls import url
from django.contrib import admin
from studentformapp import views
from django.conf import settings

urlpatterns = [
    url('', views.index, name='index'),
]
