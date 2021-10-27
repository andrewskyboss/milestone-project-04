"""
thecube_gym_fitness_club Home app view file
"""
from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view for index page """
    return render(request, 'home/index.html')
