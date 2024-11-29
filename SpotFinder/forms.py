from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Pessoa

class PessoaCreationForm(UserCreationForm):
    telefone = forms.CharField(required=False, max_length=11, help_text='Opcional')
    class Meta:
        model = Pessoa
        fields = ['username', 'email', 'telefone', 'password1', 'password2']
class PessoaLoginForm(AuthenticationForm):
    class Meta:
        model = Pessoa
        fields = ['username', 'password']