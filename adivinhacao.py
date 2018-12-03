print("***********************************")
print("*Bem vindo ao jogo de adivinhação!*")
print("***********************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1

for rodada in range (1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! Seu chute foi menor que o número secreto.")
    
    rodada = rodada + 1

print("Fim do Jogo")