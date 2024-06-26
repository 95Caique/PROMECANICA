from django.shortcuts import render
from django.http import HttpResponse
import re
from datetime import datetime


from .models import Cliente, Carro


def clientes(request):
    if request.method == "GET":
        return render(request, 'clientes.html', {'data': datetime(day=22, month=3, year=2015, hour=10, microsecond=2)})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placas')
        anos = request.POST.getlist('ano')

        cliente = Cliente.objects.filter(cpf=cpf)

        if cliente.exists():
            #TODO: Adicionar mensagem

            return HttpResponse('Cliente já cadastrado')

        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            # TODO: Adicionar mensagens
            return HttpResponse('Email inválido')

    cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )
    cliente.save()

    for carro, placa, ano in zip(carros, placas, anos):
        carro = Carro(carro=carro, placa=placa, ano=ano, cliente=cliente)
        carro.save()

        #Renderizar template
        return HttpResponse('teste')
    for carro, placa, anos in zip(carros, placas, anos):
        car = Carro(carro=carro, placa=placa, ano=anos, cliente=cliente)
        car.save


