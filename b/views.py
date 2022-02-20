from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from b.forms import *
from b.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def registerview(request):
    if request.method == 'POST':
        Home_Model.objects.create(
            name = request.POST['name'],
            username = request.POST['username'],
            password = request.POST['password'],
        )
        messages.success(request,'Thanks for Registering...! Have a nice day..!')
        return redirect('login')
    return render(request,'register.html')

def loginview(request):
    if request.method=='POST':
        user=request.POST['username']
        pas=request.POST['password']
        user1=authenticate(username=user,password=pas)
        if user1 is not None:
            login(request,user1)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request,'login.html')
