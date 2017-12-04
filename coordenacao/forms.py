from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Coordenador, Curso


class CadastrarUsuarioForm(UserCreationForm):
    # se um form so precisaria de matricula e senha, como faria a autenticaçao?
   username = forms.CharField(max_length=14, required=True)
   senha = forms.CharField(max_length = 14)
   nome = forms.CharField(max_length = 200)
   email = forms.CharField(max_length = 100)
   telefone = forms.CharField(max_length =11)
   funcao = forms.ChoiceField(('0','1'))

   class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

        def save(self, commit=True):
             # como reincorporar considerando que eu precisaria de
             user = super(CadastrarUsuarioForm, self).save(commit=False)
             user.username = matricula
             user.email = email
             user.is_active = true
             if commit:
                 user.save()

                 usuario = Coordenador()
                 usuario.user = user

                 if commit:
                     usuario.save()

                     return user
