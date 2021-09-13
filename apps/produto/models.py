from django.db import models
from django.urls import reverse


class Produto(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.CharField(max_length=100, blank=False, null=False)
    valor = models.FloatField(blank=False, null=False)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('listar_produtos')