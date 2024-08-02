from django.contrib import admin
from .models import Treinos, Exercicios, UserProfile

admin.site.register(Treinos)
admin.site.register(Exercicios)
admin.site.register(UserProfile)
