from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
#makemigrations no console, joga todas as classes de todos os app de cada arquivo models para pasta migrate,
#001_initial.py referente ao app
#migrate sobe o arquivo 0001_initial para o banco desejado.

class Produto(models.Model):                                     
    nome = models.CharField(max_length=100)                     
    quantidade = models.IntegerField()                     
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.CharField(max_length=100)
    Status = models.BooleanField()
