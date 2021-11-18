"""
thecube_gym_fitness_club Home app URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('activities/', views.activities, name='activities'),
    path('contact/', views.contact, name='contact'),
    path('gym/', views.gym, name='gym'),
    path('timetable/', views.timetable, name='timetable'),
]
