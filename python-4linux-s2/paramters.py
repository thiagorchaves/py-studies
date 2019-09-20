def cadastro(**pessoa):
    print ("O usuario {} {} foi cadastrado com sucesso!".format(pessoa['nome'], pessoa['sobrenome']))
cadastro(nome='thiago', sobrenome='chaves', idade=36)

exit()



def soma(*num):
    return (sum(num))

s = soma(5,3,7,12,56,78,90,100)
print(s)