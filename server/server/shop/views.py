from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.contrib import auth
from django.contrib.auth import authenticate, login
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

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username, email, password1)
            user.save()
            auth.login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'success': 'Account created successfully. Please log in.'})
    return render(request,'register.html')
        

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def email_req(request):
    if request.method == 'post':
        email = request.POST['email']
        user = User.objects.filter(email=email)
        if user.exists():
            return render(request, 'email_req.html', {'success': 'An email has been sent to the provided address.'})
        else:
            return render(request, 'email_req.html', {'error': ''})

# Create your views here.

