import random


def jogar():

    print("\n")
    print("*********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("*********************************")

    pontos = 1000
    pontos_perdidos = 0
    #int(random.random()*100)
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3

    print("Qual o nível de dificuldade?")
    print("(1) Fácil")
    print("(2) Moderado")
    print("(3) Difícil")

    nivel = int(input("Digite o nível:"))
    print("Você selecionou o nível:", nivel)

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # while (rodada <= total_de_tentativas):
    for rodada in range (1, total_de_tentativas + 1):
        print("\n[Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = input("Digite o seu numero (maior que 1 e menor que 100:")
        print("Você digitou:", chute)

        chute = int(chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número maior que 1 e menor que 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("\n\t~Você acertou!")
            break;
        else:
            if(maior):
                print("\n\t~Você errou! O seu chute foi maior que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
            elif(menor):
                print("\n\t~Você errou! O seu chute foi menor que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("\n\n")
    print("*********************************")
    print("Fim do jogo")
    print("*********************************")
