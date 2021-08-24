from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.CharField('Email', max_length=150)

#Criar outra classe persistente
