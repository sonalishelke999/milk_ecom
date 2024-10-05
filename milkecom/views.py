from django.shortcuts import render
from userlogin.models import UserLogin
# Create your views here.

def homepage(req):
    if req.method == "GET":
        return render(req, "homepage.html")
    
def register(req):
    if req.method == "GET":
        return render(req, "register.html")
    if req.method == "POST":
        firstname=req.POST.get('firstname')
        lastname=req.POST.get('lastname')
        email=req.POST.get('email')
        mobilenumber=req.POST.get('mobilenumber')
        password=req.POST.get('password')
        user=UserLogin(firstname=firstname,lastname=lastname,email=email,mobile=mobilenumber,password=password)
        user.save()
        return render(req, "mainpage.html")
    
def login(req):
    if req.method == "GET":
        return render(req, "login.html")
    if req.method == "POST":
        email=req.POST.get('email')
        print(email)
        user=UserLogin.objects.get(email=email)
        if user:
            return render(req, "mainpage.html")
        else:
            return render(req, "homepage.html")
    
def mainpage(req):
    if req.method == "GET":
        return render(req, "mainpage.html")