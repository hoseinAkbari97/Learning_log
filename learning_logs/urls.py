"""Defines URL  patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpattern = [
    # Home page
    path('', views.index, name='index'),
]