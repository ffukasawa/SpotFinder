from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
def home(request):
    return render(request, 'index.html')

def login(request):
    return(render(request,"SignIn.html"))

def cadastro(request):
    return(render(request,"SignUp.html"))

def pag_inicial_prelogin(request):
    if request.method=='POST':
        if 'Login' in request.POST:
            return redirect ('pagina_signin.html')
        elif 'Sign up' in request.POST:
            return redirect ('pagina_signup.html')
        elif 'Continue without logging in' in request.POST:
            return redirect('pagina_inicial.html')
    return render(request,'pagina_prelogin.html')

def pag_signin(request):
    if request.method=='POST':
        login=request.POST['login']
        password=request.POST['password']
        user= authenticate(request,login=login,password=password)
        if user is not None:
            login(request,user)
            return redirect('pagina_inicial.html')
        else:
            messages.error(request,'Usuário o senha inválidos.')
    return render(request,'pagina_signin.html')

def pag_signup(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        if(password != confirmpassword):
            messages.error(request,'As senhas não coincidem.')
            return redirect('pagina_signup.html')
        user=User.objects.create_user(username=fullname,email=email,password=password)
        login(request,user)
        return redirect('pagina_inicial.html')
    return render(request,'pagina_signup.html')

def pag_inicial(request):
    return render(request,'pagina_inicial')

def pag_busca(request):
    if request.method=='POST':
        if 'Aonde você quer parar?' in request.POST:
            return 
    return render(request,'pagina_busca')

def pag_menu(request):
    return render(request,'pagina_menu')

def pag_ajustes(request):
    if request.method=='POST':
        if 'Ativar Notificações' in request.POST:
            return 
        elif 'Alterar idioma' in request.POST:
            return 
        elif 'Reportar bugs' in request.POST:
            return 
        elif 'Suporte ao usuário' in request.POST:
            return 
        elif 'Sair da conta' in request.POST:
            return redirect ('pagina_prelogin.html')
    return render(request,'pagina_ajustes')

def pag_historico(request):

    return render(request,'pagina_historico')

def pag_perfil(request):
    profile=request.user.profile
    if request.method=='POST':
        telefone=request.POST['telefone']
        medidasdoveiculo=request.POST['medidasdoveiculo']
        profile.telefone=telefone
        profile.medidasdoveiculo=medidasdoveiculo
        profile.save()
        messages.success(request,'Seu perfil foi atualizado.')
        return redirect('pagina_inicial.html') 
    return render(request,'pagina_perfil.html')

def pag_filtros(request):
    return render (request,'pagina_filtros.html')

def pag_favoritos(request):
    return render(request,'pagina_favoritos.html')

def pag_espdisp(request):
    return render (request,'pagina_espdisp.html')



