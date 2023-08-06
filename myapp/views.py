from django.shortcuts import render,redirect

# Create your views here.

def Home(request):
    return render(request,"Home.html")

def logout(request):
    return render(request,"logout.html")

def Contact(request):
    return render(request,"Contact.html")
def signup(request):
    return render(request,'signUp.html')

def index(request):
    return render(request,"index.html")
def login(request):
    return render(request, 'login.html')  # Create a corresponding HTML template
