#!/usr/bin/python3

ling = input('Qual a melhor linguagem de programação?')

try:
    if ling.lower().strip() == 'python':
        print('Você acertou')
    else:
        raise ValueError('Linguagem errada')
except ValueError as e:
    print ('Erro {}'.format(e))

