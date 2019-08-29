#!/usr/bin/python3
idade = int(input("Digite sua idade = "))
habilitacao = input("Você é habilitado? ")
if habilitacao.lower().strip() == 'sim':
    habilitacao = True
else:
    instrutor = input('Voce está acompanhado de um instrutor?')
    if instrutor.lower().strip() == 'sim':
        dirigir = True
if idade >= 18 and habilitacao == True:
    print('Você pode dirigir')
elif instrutor == True:
    print("Boa Aula!")
else:
    print('Você não pode dirigir')