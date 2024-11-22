from django.shortcuts import render

def login(request):
    return(render(request,"SignIn.html"))

def cadastro(request):
    return(render(request,"SignUp.html"))



# Create your views here.
