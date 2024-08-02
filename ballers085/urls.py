from django.urls import path
from django.shortcuts import render
from django.conf.urls import handler404
from .views import ballers085_redirect, hoop, index,base_teste, login_view, profile, profile_link, register,treino_exercicio, treinos, treinos_categoria, psicobaska

def custom_404(request, exception):
    return render(request, '404.html', status=404)

urlpatterns = [
    path('', index, name='index'),
    path('hoop/', hoop, name='hoop'),
    path('treinos/<str:categoria>/', treinos_categoria, name='treinos_categoria'),
    path('treinos/<str:categoria>/<str:nome_treino>', treino_exercicio, name='treino_exercicio'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('ballers085/', ballers085_redirect, name='ballers085_redirect'),
    path('login/', login_view, name='login'),  # Adiciona a URL de login
    path('psicobaska/', psicobaska, name='psicobaska'),  # Adiciona a URL de login
    path('profile_link/<str:usuario>', profile_link, name='profile_link'),  # Adiciona a URL de login
    path("base_teste/", base_teste, name="base_teste"),
]
handler404 = custom_404

