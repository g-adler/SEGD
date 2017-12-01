# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Coordenador

# Create your views here.
def index (request):
        coords = Coordenador.objects.all()
        from django.conf import settings
        return render(request, 'coordenacao/index.html', {})
