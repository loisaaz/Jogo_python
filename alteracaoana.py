print("\nBEM VINDO AO JOGO DA ADIVINHAÇÃO!!")
print("\nO objetivo é acertar o número secreto.")
print("\nVocê tem 10 tentativas para acertar o número secreto entre [1000 e 9999]")
print("\n(OBS: A partir da 5° tentativa o jogo irá te ajudar com  dicas!)")
print("\n>>>TECLE ALGO PARA CONTINUAR <<<<")
input() # tecle algo para aparecer a próxima tela

import random

jogar_novamente = 1

while jogar_novamente == 1:
    codigo = random.randint(1000, 9999)
    tentativas = 0
    ganhou = 0

    # Variáveis para armazenar os dígitos corretos encontrados
    pos1 = -1
    pos2 = -1
    pos3 = -1
    pos4 = -1

    while tentativas < 10 and ganhou == 0:
        print("\n---------------------------------------")
        jogador = int(input("Digite um número de 4 dígitos: "))
        print()

        acertos = 0
        posicao = 0

        temp_codigo = codigo
        temp_jogador = jogador

        # Separar os dígitos para facilitar comparações
        codigo_dig1 = (codigo // 1000) % 10
        codigo_dig2 = (codigo // 100) % 10
        codigo_dig3 = (codigo // 10) % 10
        codigo_dig4 = codigo % 10

        jog_dig1 = (jogador // 1000) % 10
        jog_dig2 = (jogador // 100) % 10
        jog_dig3 = (jogador // 10) % 10
        jog_dig4 = jogador % 10

        # Verificar posição 1
        if jog_dig1 == codigo_dig1:
            posicao += 1
            pos1 = jog_dig1

        # Verificar posição 2
        if jog_dig2 == codigo_dig2:
            posicao += 1
            pos2 = jog_dig2

        # Verificar posição 3
        if jog_dig3 == codigo_dig3:
            posicao += 1
            pos3 = jog_dig3

        # Verificar posição 4
        if jog_dig4 == codigo_dig4:
            posicao += 1
            pos4 = jog_dig4

        # Contar acertos fora da posição correta
        for cont in range(4):
            resto_jogador = temp_jogador % 10

            numero = codigo
            for conta in range(4):
                resto_numero = numero % 10

                if resto_jogador == resto_numero:
                    acertos += 1

                numero = numero // 10

            temp_jogador = temp_jogador // 10

        tentativas += 1

        print("Espaços descobertos:")
        if pos1 != -1:
            print(pos1, end=" ")
        else:
            print("_", end=" ")

        if pos2 != -1:
            print(pos2, end=" ")
        else:
            print("_", end=" ")

        if pos3 != -1:
            print(pos3, end=" ")
        else:
            print("_", end=" ")

        if pos4 != -1:
            print(pos4)
        else:
            print("_")

        print("\nTentativas restantes:", 10 - tentativas)
        print("\nNúmeros corretos na posição certa:", posicao)
        print("\nNúmeros corretos na posição errada:", acertos - posicao)

        # Dicas a partir da 5ª tentativa
        if tentativas >= 5 and ganhou == 0:
            if pos1 == -1:
                if codigo_dig1 >= 5:
                    print("\n(DICA: O número na posição 1 é maior ou igual a 5)")
                else:
                    print("\n(DICA: O número na posição 1 é menor que 5)")
            elif pos2 == -1:
                if codigo_dig2 >= 5:
                    print("\n(DICA: O número na posição 2 é maior ou igual a 5)")
                else:
                    print("\n(DICA: O número na posição 2 é menor que 5)")
            elif pos3 == -1:
                if codigo_dig3 >= 5:
                    print("\n(DICA: O número na posição 3 é maior ou igual a 5)")
                else:
                    print("\n(DICA: O número na posição 3 é menor que 5)")
            elif pos4 == -1:
                if codigo_dig4 >= 5:
                    print("\n(DICA: O número na posição 4 é maior ou igual a 5)")
                else:
                    print("\n(DICA: O número na posição 4 é menor que 5)")

        if posicao == 4:
            ganhou = 1
            print("\n---------------------------------------")
            print("\nPARABÉNS! VOCÊ DESCOBRIU O NÚMERO SECRETO!")
            print("Tentativas:", tentativas)

    if ganhou == 0:
        print("\n---------------------------------------")
        print("\nVOCÊ NÃO ACERTOU O NÚMERO SECRETO :(")
        print("\nO código secreto era:", codigo)

    jogar_novamente = int(input("\nDeseja jogar novamente? (1 - Sim / 0 - Não): "))
    print("Obrigado por jogar!")
