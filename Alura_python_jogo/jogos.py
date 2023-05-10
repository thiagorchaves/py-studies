import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*********Escolha o Jogo!*********")
    print("*********************************")

    print("(1) Forca, (2) Adivinhacao")

    jogo = int(input("Qual jogo deseja jogar? "))

    if jogo == 1:
        print("Jogando Forca")
        forca.jogar()
    else:
        print("Jogando Adivinhacao")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo ()