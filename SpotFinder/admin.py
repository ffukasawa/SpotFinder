from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Pessoa

class PessoaAdmin(UserAdmin):
    list_display = ('username', 'email', 'telefone')


admin.site.register(Pessoa, PessoaAdmin)

