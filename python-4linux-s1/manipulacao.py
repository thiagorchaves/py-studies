#!/usr/bin/python3
# para escrita do arquivo
with open('frutas.txt', 'w') as arq:
    arq.write('limao\n')
    arq.write('laranja\n')
    arq.write('acerola\n')
    arq.write('jabuticaba\n')
#Para leitura

with open('frutas.txt', 'r') as arq:
    print(arq.read())

# gravação de elementos com quebra de linha sem sobrescrever
nomes = ['joao', 'maria', 'pedro']

with open ('nomes.txt', 'x') as arq:
    for nome in nomes:
        arq.write(nome + '\n')