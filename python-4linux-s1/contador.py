#!/usr/bin/python3

cont = 0

while True:
    print('Execução {}'.format(cont))
    if cont == 100:
        print('Encerrando o loop')
        break
    cont += 1