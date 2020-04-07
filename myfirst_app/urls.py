from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from myfirst_app import views
appname='first_app'
urlpatterns = [
    path('',views.index,name='view'),

]
