# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Coordenador

# Create your views here.
def index (request):
        coords = Coordenador.objects.all()
        # func = Funcionario.objects.all()
        from django.conf import settings
        return render(request, 'coordenacao/index.html', {})

def pg_coord(request):
    from django.conf import settings

    return render(request, 'coordenacao/c_home.html')

def pg_direc(request):
    from django.conf import settings

    return render(request, 'coordenacao/d_home.html')
