from asyncio.windows_events import NULL
from django.db import models



class Produto(models.Model):                                     
    nome = models.CharField(max_length=100)                     
    quantidade = models.IntegerField()                     
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.CharField(max_length=100)
    Status = models.BooleanField()
