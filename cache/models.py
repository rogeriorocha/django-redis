
from __future__ import unicode_literals
from django.db import models

import datetime
# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=120,unique=True)
    descricao = models.TextField(null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True)
    data_alteracao = models.DateTimeField(auto_now=True, blank=True)
    valor = models.IntegerField(null=True, blank=True)
 
    def __unicode__(self):
        return self.nome
 
    def to_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'valor': self.valor,
            'data_criacao': self.data_criacao,
            'data_alteracao': self.data_alteracao
        }