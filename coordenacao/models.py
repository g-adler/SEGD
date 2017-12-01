# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

LISTA_TIPO_DOC = (
	('0', 'PDF'),('1','WORD'),)

# IS_COORD = (
# 	('0', 'DIRECAO'),('1','COORDENACAO')
# )
class Funcionario (models.Model):
	matricula = models.CharField(max_length = 30)
	nome = models.CharField(max_length = 200)
	email = models.CharField(max_length = 100)
	telefone = models.CharField(max_length =11)
	# funcao = models.CharField(max_length =1, choices = IS_COORD)

	def __str__(self):
		return self.nome

class Documento (models.Model):
	coordenador = models.ForeignKey(Coordenador , on_delete=models.CASCADE)
	titulo = models.CharField(max_length =50)
	tipo = models.CharField(max_length =1, choices = LISTA_TIPO_DOC, default='0')
	def __str__(self):
		return self.titulo

class Curso (models.Model):
	titulo = models.CharField(max_length =50)
	coordenador = models.ForeignKey(Coordenador , on_delete=models.CASCADE)

	def __str__(self):
		return self.titulo
