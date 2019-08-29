#!/usr/bin/python

nomes = ['daniel', 'andre', 'pedro', 'joao']
busca = input('Digite o nome do convidado:')
for nome in nomes:
    if busca.lower().strip() == nome:
        print('Convidado está na lista')
        break
else:
    print('Convidado não está na lista')