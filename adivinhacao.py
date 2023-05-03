print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = input("Digite o seu numero: ")

print("Você digitou", chute)

chute = int(chute)

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if acertou:
    print ("Você Acertou!")
else:
    if(maior):
        print ("Você errou! O seu chute foi maior que o numero secreto")
    elif(menor):
        print ("Você errou! O seu chute foi menor que o numero secreto")

print ("Fim do Jogo!")