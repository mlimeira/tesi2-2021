from django.db import models
from stdimage import StdImageField

# Create your models here.
#Entidade Forte
class Contato(models.Model):
    telefone = models.CharField('Telefone', max_length=13)
    def __str__(self):
        return self.telefone
    """
    Relacionamentos
    Um para Um: um contato se relaciona com apenas um clientee
    um cliente com apenas um contato
    """

#Entidade Fraca
class Cliente(models.Model):
    contato = models.OneToOneField(Contato, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.CharField('Email', max_length=150)
    def __str__(self):
        return "{} {}".format(self.nome, self.sobrenome)

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    imagem = StdImageField('imagem', upload_to='produtos', variations={'thumb': (90, 90)})
    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ManyToManyField(Produto)
    def __str__(self):
        return "{}: {}".format(self.pk, self.cliente.nome)


