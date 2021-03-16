from django.db import models


class Produto(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.CharField(max_length=200)
    curtidas = models.PositiveIntegerField(default=0)


class Usuario(models.Model):
    pass
