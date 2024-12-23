from django.shortcuts import render

# Create your views here.

def home(request):
    v = "This is my new home page"
    return render(request,'home.html',{'data':v})

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')
