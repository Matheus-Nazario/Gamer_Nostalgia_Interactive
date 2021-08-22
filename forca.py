import random


def jogar():

    apresentacao()  # aprestenção Bem-vindo

    palavra_secreta = (
        carregar_palavra_secreta()
    )  # carregando a palavra secreta
    letras_acertadas = inicializar_letras_acertadas(
        palavra_secreta
    )  # [_ _ _ _] colocanto letras acertadas

    print(letras_acertadas)  # imprimir a quantida [ _ _ _ _ _ _]

    enforcou = False
    acerto = False
    erros = 0

    while not enforcou and not acerto:  # enquanto não enforcou e não acerto
        chute = pede_cute()  # chute do userClaro
        if (
            chute in palavra_secreta
        ):  # se a letra estivar na palavra \ se acertou
            marca_indice_chute_correto(
                chute, palavra_secreta, letras_acertadas
            )
        else:
            erros += 1
            desenha_forca(erros)
        enforcou = erros == 7  # quantidade de erros é 7
        acerto = (
            "_" not in letras_acertadas
        )  # Quando acabar [_ _ _ _] "_" acertou

        print(letras_acertadas)
    if acerto:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")


def apresentacao():
    print(" ")
    print("---------------------------------")
    print("---Bem vindo ao jogo da Forca!---")
    print("---------------------------------")
    print(" ")


def carregar_palavra_secreta():

    arquivo = open("lista_frutas.txt", "r")  # abrindo o arquivo de palavras
    palavras = []  # criando lista da plavra

    for linha in arquivo:
        linha = linha.strip()  # tirando os espaçoes
        palavras.append(linha)
        # inluindo a linha na lista e limpando ex: [morango]
        # incluido da linha palavra

    arquivo.close()  # fechando o arquivo

    num = random.randrange(
        0, len(palavras)
    )  # numero aletario pela quantidade palavras que tem no arqruivo
    palavra_secreta = palavras[num].upper()  # palavra secreta

    return palavra_secreta


def inicializar_letras_acertadas(palavra):
    return ["_" for linha in palavra]


def pede_cute():
    chute = input("Qual letra? ")
    chute = (
        chute.strip().upper()
    )  # tirarando os espaços e deixando tudo maisculo
    return chute


def marca_indice_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0  # indice começa com 0
    for letra in palavra_secreta:  # verificar cada letar por palavra
        if chute == letra:  # se a letra  chutada é igual a letra
            letras_acertadas[index] = letra  # pegar a letra a acertada
        index += 1  # incluir e verificar toso indices


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
