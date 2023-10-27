from django.shortcuts import render
from .models import Product
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'index.html')


#def product(request):
    #data = Product.objects.all().values()
