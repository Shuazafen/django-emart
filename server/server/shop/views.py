from django.shortcuts import render, get_object_or_404
from django.conf.urls.static import static
from .models import *

def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})

def detail(request, model_name,pk):
    model = None
    if model_name == "product":
        model = get_object_or_404(Product, pk=pk)
    context = {"model":model}
    return render(request, "detail.html", context)


def order(request):
    products = Product.objects.all()
    return render(request, 'order.html', {'products':products})
# Create your views here.

