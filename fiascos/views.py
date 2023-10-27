from django.shortcuts import render
from fiascos.models import Product
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'index.html')

def entry(request):
    return render(request, 'entry.html')

def working(request):
    return render(request, 'working.html')

def archive(request):
    products = Product.objects.all()
    #import pdb;pdb.set_trace()
    return render(request, 'archive.html', context={"products":products})

def basepost(request, product_id:int):
    product = Product.objects.filter(id=product_id).first()
    return render(request, 'basepost.html', context={"product":product})


#def product(request):
    #data = Product.objects.all().values()
