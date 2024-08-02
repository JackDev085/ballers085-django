from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
import re
from django.contrib.auth.forms import AuthenticationForm


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nome_completo', 'link_foto_perfil']
class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    nome_completo = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'nome_completo']

    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        if re.match(r'^[^a-zA-Z]', username):
            raise forms.ValidationError('O nome de usuário não pode começar com um caractere especial.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está em uso. Por favor, escolha um email diferente.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username'].lower()
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user_profile = UserProfile.objects.create(
                user=user,
                nome_completo=self.cleaned_data['nome_completo'],
            )
            user_profile.save()
        return user
