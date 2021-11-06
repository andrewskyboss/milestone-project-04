"""thecube_gym_fitness_club products URL Configuration
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('', views.all_plans, name='plans'),
]
