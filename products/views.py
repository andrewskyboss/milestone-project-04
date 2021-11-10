"""thecube_gym_fitness_club products views Configuration
"""

from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def all_plans(request):
    """ A view to show all plans, including sorting and search queries """
    plans = Product.objects.all()

    context = {
        'plans': plans,
    }
    return render(request, 'products/plans.html', context)
