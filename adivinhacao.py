import random


def jogar():

    apresentacao()

    numero_secreto = numero_aleatorio_1_ao_100()
    pontos = 1000
    nivel = perguntando_nivel_jogo()
    total_tetantativas = totais_de_tentativas(nivel)

    for rodada in range(1, total_tetantativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tetantativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou ", chute)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print(
                    "Você errou! O seu chute foi maior do que o número secreto."
                )
            elif menor:
                print(
                    "Você errou! O seu chute foi menor do que o número secreto."
                )
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


def apresentacao():
    print("---------------------------------")
    print("------ JOGO DA ADIVINHAÇÃO ------")
    print("---------------------------------")


def numero_aleatorio_1_ao_100():
    return random.randrange(1, 101)


def perguntando_nivel_jogo():
    print(" ")
    print("Qual é o nível de dificuldade? ")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o Nível:"))
    return nivel


def totais_de_tentativas(nivel):
    if nivel == 1:
        totais_de_tentativas = 20
    elif nivel == 2:
        totais_de_tentativas = 10
    elif nivel == 3:
        totais_de_tentativas = 5

    return totais_de_tentativas


if __name__ == "__main__":
    jogar()
