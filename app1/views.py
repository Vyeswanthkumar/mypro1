from django.shortcuts import render,HttpResponse,redirect
from .forms import StudentForm

# Create your views here.

def home(request):
    v = "This is my new home page"
    return render(request,'home.html',{'data':v})

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def insert(request):
    st=StudentForm()
    if request.method=='POST':
        s=StudentForm(request.POST)
        if s.is_valid():
            s.save()
            return redirect('display')
    return render(request,'insert.html',{'form':st})

from .models import Student
def display(request):
    v=Student.objects.all()
    return render(request,'display.html',{'data':v})