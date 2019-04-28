import forca
import adivinhacao

def escolhe_jogo():

    print("\n")
    print("*********************************")
    print("*********Escolha seu jogo********")
    print("*********************************")

    print("(1) Adivinhacao")
    print("(2) Forca")

    jogo = int(input("Digite o jogo:"))

    if (jogo == 1):
        print("Você selecionou o jogo: Adivinhacao!")
        adivinhacao.jogar()
    elif (jogo == 2):
        print("Você selecionou o jogo: Forca!")
        forca.jogar()
    else:
        print("Esse jogo não existe!")


if (__name__ == "__main__"):
    escolhe_jogo()