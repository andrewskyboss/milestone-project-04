from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view for index page """
    return render(request, 'home/index.html')
