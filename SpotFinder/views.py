from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Pessoa
from .forms import PessoaCreationForm,PessoaLoginForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = PessoaLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)  # login importado de django.contrib.auth
                return redirect('home')
    else:
        form = PessoaLoginForm()
    return render(request, 'SignIn.html', {'form': form})

def cadastro(request):
    if request.method == 'POST':
        form = PessoaCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o usuário no banco
            login(request, user)  # Realiza o login automático
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = PessoaCreationForm()  # Cria o formulário vazio para GET

    return render(request, 'SignUp.html', {'form': form})

@login_required    
def logout_view(request):
    logout(request)  # Chama o logout do Django corretamente
    return redirect('login') 
@login_required
def pag_inicial(request):
    return render(request,'pgInicial.html')

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
            return redirect ('preLogin.html')
    return render(request,'configGeral.html')

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
        return redirect('pgInicial.html') 
    return render(request,'configUsuario.html')

def pag_filtros(request):
    return render (request,'pagina_filtros.html')

def pag_favoritos(request):
    return render(request,'pagina_favoritos.html')

def pag_espdisp(request):
    return render (request,'pagina_espdisp.html')

def pag_filtros(request):
    filter_options = {
        "sizes": ["4,5m x 2,2m", "5m x 2,5m", "5,5m x 2,5m"],
        "covered": True,
        "prices": ["R$15,00", "R$15,00 - R$30,00", "Acima de R$30,00"],
    }
    return render (request,'pagina_filtros.html')

def pag_favoritos(request):
    favorites = [
        {"name": "Casa", "distance": "1.2 km"},
        {"name": "Trabalho", "distance": "0.8 km"},
        {"name": "Casa Mãe", "distance": "2.5 km"},
    ] 
    return render(request,'pagina_favoritos.html')

def pag_espdisp(request):
    return render (request,'pagina_espdisp.html')

def pag_espdisp2(request):
    return render (request,'pagina_espdisp2.html')

def pag_espdisp3(request):
    return render (request,'pagina_espdisp3.html')

def caracteristicas_vagas(request):
    locations = {
        1: {
            "name": "Rua General Urquiza",
            "slots": "30 vagas",
            "ratings": "★★★★☆",
            "security": "Alta",
            "size": "2 x 35 m",
        },
        2: {
            "name": "Av. Ataulfo de Paiva",
            "slots": "50 vagas",
            "ratings": "★★★☆☆",
            "security": "Média",
            "size": "5 x 20 m",
        },
    }
    location = locations.get(vaga_id, None)

    if not location:
        return render(request, "error.html", {"message": "Local não encontrado."})
    return render(request,'caractvagas.html')

def caracteristicas_vagas2(request):
    
    return render(request,'caractvagas2.html')

def filtros_espdisp(request):
    filter_options = {
        "sizes": ["4,5m x 2,2m", "5m x 2,5m", "5,5m x 2,5m"],
        "covered": True,
        "prices": ["R$15,00", "R$15,00 - R$30,00", "Acima de R$30,00"],
    }
    return render(request,'filtros_espdisp.html')


"""def pag_inicial_prelogin(request):
    if request.method=='POST':
        if 'Login' in request.POST:
            return redirect ('SignIn.html')
        elif 'Sign up' in request.POST:
            return redirect ('SignUp.html')
        elif 'Continue without logging in' in request.POST:
            return redirect('pgInicial.html')
    return render(request,'preLogin.html')

def pag_signin(request):
    if request.method=='POST':
        login=request.POST['login']
        password=request.POST['password']
        user= authenticate(request,login=login,password=password)
        if user is not None:
            login(request,user)
            return redirect('pgInicial.html')
        else:
            messages.error(request,'Usuário o senha inválidos.')
    return render(request,'SignIn.html')

def pag_signup(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        if(password != confirmpassword):
            messages.error(request,'As senhas não coincidem.')
            return redirect('SignUp.html')
        user=User.objects.create_user(username=fullname,email=email,password=password)
        login(request,user)
        return redirect('pgInicial.html')
    return render(request,'SignUp.html')
"""
