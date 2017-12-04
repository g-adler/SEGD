# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import CreateView

from django.shortcuts import render

from .forms import CadastrarUsuarioForm

from .models import Coordenador

# Create your views here.
def index (request):
        coords = Coordenador.objects.all()
        # func = Funcionario.objects.all()
        from django.conf import settings
        return render(request, 'coordenacao/index.html', {})

def usuario (request):
    from django.conf import settings
    return render(request, 'coordenacao/cadastro.html')

def pg_coord(request):
    from django.conf import settings

    return render(request, 'coordenacao/c_home.html')

def pg_direc(request):
    from django.conf import settings

    return render(request, 'coordenacao/d_home.html')

class CadastrarUsuario(CreateView):
    form_class = CadastrarUsuarioForm
    template_name = 'coordenacao/cadastro.html'
