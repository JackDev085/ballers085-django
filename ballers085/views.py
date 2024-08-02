from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Exercicios, Treinos, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .forms import EmailAuthenticationForm
from.forms import UserProfileForm

class CustomLoginView(auth_views.LoginView):
    authentication_form = EmailAuthenticationForm

def index(request):
    return render(request, 'index.html')

def first_page(request):
    return render(request, 'first_page.html', {'extracss':'css/first_page.css'})

@login_required
def ballers085_redirect(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redireciona para a página de login se não estiver autenticado
    else:
        return redirect('index')  # Redireciona para a página inicial se estiver autenticado
#===============================
def base_teste(request):
    return render(request, 'base_teste.html', {'extracss':'css/base_teste.css'})
#===============================

@login_required
def treinos(request):
    return render(request, 'treinos.html', {'extracss':'css/treinos.css'})


def psicobaska(request):
    return render(request, 'psicomotor/psicobaska.html', {'extracss':'css/psicobaska.css'})

@login_required
def hoop(request):
    return render(request, 'hoop.html', {'extracss':'css/hoop.css'})

@login_required
def treinos_categoria(request, categoria):
    treinos = Treinos.objects.filter(categoria=categoria)
    if categoria =="academia":
        return render(request, 'treinos_academia.html', {'extracss':'css/treinos_academia.css', 'treinos': treinos, 'categoria': categoria})  
    return render(request, 'treinos.html', {'extracss':'css/treinos.css', 'treinos': treinos, 'categoria': categoria})


@login_required
def treino_exercicio(request, nome_treino, categoria):
    treino_escolhido = Treinos.objects.filter(caminho_treino_url=nome_treino)
    categoria = categoria
    exercicios = []
    exercicio1 = None
    try:
        exercicios = Exercicios.objects.filter(treino_id=treino_escolhido[0].id)
        if exercicios:
            exercicio1 = exercicios[0]
    except Exception as e:
        print(f"Error: {e}")
        return render(request,"404.html")
    return render(request, 'exercicios.html', {'extracss': 'css/exercicios.css', 'exercicios': exercicios, 'exercicio1': exercicio1})


@login_required
def profile(request):
    try:
        usuario = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        usuario = UserProfile(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=usuario)

    return render(request, 'profile.html', {
        'extracss': 'css/profile.css',
        'user_perfil': usuario,
        'form': form
    })

@login_required
def profile_link(request, usuario):
    try:
        usuario = User.objects.filter(username=usuario)
        usuario1 = UserProfile.objects.filter(user_id=usuario[0].id)
    except:
        return render(request,"404.html")
    return render(request, 'profile_perfil.html', {'extracss':'css/profile.css', 'usuario': usuario1[0]})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'extracss':'css/login.css'})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redireciona para a página inicial após o login bem-sucedido
                return redirect('index')
            else:
                # Retorna uma mensagem de erro se a autenticação falhar
                messages.error(request, "Login inválido. Tente novamente.")
        else:
            # Formulário inválido
            messages.error(request, "Formulário inválido. Tente novamente.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

