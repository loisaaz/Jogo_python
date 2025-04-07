print("\nBEM VINDO AO JOGO SECRETO!!")
print("\nO objetivo é acertar o número secreto.")
print("\nVocê 10 tentativas para acertar o número secreto entre [1000 e 9999]")
print("\nA partir da 5° tentativa o jogo irá te ajudar com  dicas")
print("\n>>>TECLE ALGO PARA CONTINUAR <<<<:")
input() # tecle algo para aparecer a próxima tela

import random 
codig_secret= random.randint(1000,9999) #biblioteca

tentativas = 0 # loop para contagem de tentativas
max_tentativas = 10
jogar_novamente = 1

while jogar_novamente == 1:
    codigo = random.randint(1000, 9999)
    tentativas = 0
    ganhou = 0

    while tentativas < 10 and ganhou == 0:
        jogador = int(input("Digite um número de 4 dígitos: "))

        # Aqui é para contar acertos e posições corretas
        acertos = 0
        posicao = 0
        
        # Verifica cada dígito, igual como a Helo fez no outro arquivo
        for contador in range(4):
            resto_jogador = jogador % 10
            resto_codigo = codigo % 10

            # Verifica posição correta
            if resto_jogador == resto_codigo:
                posicao += 1

            # Verifica se o número existe no código
            numero = codigo
            for contagem in range(4):
                resto_numero = numero % 10

                if resto_jogador == resto_numero:
                    acertos += 1

                numero //= 10

            jogador //= 10
            codigo //= 10

        tentativas += 1

        print("Números corretos na posição certa:", posicao)
        print("Números corretos na posição errada:", acertos - posicao)

        # Verifica se ganhou
        if posicao == 4:
            ganhou = 1
            print("Parabéns! Você acertou o código secreto!")
            print("Tentativas:", tentativas)


