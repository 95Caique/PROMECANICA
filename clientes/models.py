from django.db import models
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.nome

class Carro(models.Model):
    carro = models.CharField(max_length=50)
    ano = models.IntegerField()
    placa = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lavagens = models.IntegerField(default=0)
    consertos = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.nome

