from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class CadastrarUsuarioForm(UserCreationForm):
    # se um form so precisaria de matricula e senha, como faria a autenticaçao?
    matricula = forms.CharField(max_length=14, required=True)
    senha = forms.
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        # como reincorporar considerando que eu precisaria de
        user = super(CadastrarUsuarioForm, self).save(commit=False)
        user.username = limpar_mascara(self.cleaned_data['username'])
        user.email = self.cleaned_data['email']
        user.is_active = False
        if commit:
            user.save()

        usuario = Usuario()
        usuario.user = user
        usuario.nome_usuario = self.cleaned_data['nome_usuario']
        codigo_ativacao = get_random_string()
        usuario.codigo_ativacao = codigo_ativacao
        if commit:
            usuario.save()

        return user
