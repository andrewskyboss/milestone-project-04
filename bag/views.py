"""thecube_gym_fitness_club bag views Configuration
"""
from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')
