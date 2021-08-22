import adivinhacao
import forca


def jogar():
    apresentacao()

    jogo = int(input("Qual é o jogo que você deseja? "))
    logica_escolha_jogo(jogo)


def logica_escolha_jogo(jogo):
    if jogo == 1:
        print("Jogando a Forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando a Adivinhaçao")
        adivinhacao.jogar()
    return


def apresentacao():
    print("*********************************")
    print("****** Escolha o seu jogo! ******")
    print("*********************************")
    print()
    print("(1) Jogo da Forca *** (2) Jogo da Adivinhação ")
    print()


if __name__ == "__main__":
    jogar()
