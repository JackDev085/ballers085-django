from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
import re

def validate_username(username):
    if re.match(r'^[^a-zA-Z]', username):
        raise ValidationError('O nome de usuário não pode começar com um caractere especial.')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, max_length=30, unique=True)
    nome_completo = models.CharField(max_length=30)
    data_criacao = models.DateTimeField(auto_now_add=True)
    link_foto_perfil = models.CharField(max_length=100, default='imgs/usuarios/default.jpg')
    
    def save(self, *args, **kwargs):
        self.user.username = self.user.username.lower()
        validate_username(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.user.username

class Treinos(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    descricao = models.TextField(max_length=40)
    duracao = models.CharField(max_length=30)
    link_video_treino = models.CharField(max_length=50, default="RpC7sv8_LIg")
    criador = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='treinos',default=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=30, default='Treino')
    caminho_treino_url = models.CharField(max_length=30, default='nome_treino')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nome

class Exercicios(models.Model):
    nome = models.CharField(max_length=30)
    repeticoes = models.CharField(max_length=30)
    treino = models.ForeignKey(Treinos, on_delete=models.CASCADE, related_name='exercicios')
    link = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nome
