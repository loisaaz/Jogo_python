print("\nBEM VINDO AO JOGO SECRETO!!")
print("\nO objetivo é acertar o número secreto.")
print("\nVocê 10 tentativas para acertar o número secreto entre [1000 e 9999]")
print("\nA partir da 5° tentativa o jogo irá te ajudar com  dicas")
print("\n>>>TECLE ALGO PARA CONTINUAR <<<<:")
input()

import random 
codig_secret= random.randint(1000,9999) 

tentativas = 0 
max_tentativas = 10
#acertos = 0
#posicao = 0
progresso = "_ _ _ _"
prog_digito_1 = "_"
prog_digito_2 = "_"
prog_digito_3 = "_"
prog_digito_4 = "_"

while tentativas < max_tentativas:
    print("\n---------------------------------------")
    palpite = int(input("Digite seu palpite sendo um número de 4 dígitos:"))
    if palpite < 1000 or palpite > 9999:
        print("\nATENÇÃO! ! !")
        print("\nINSIRA UM VALOR NO INTERVALO DE 1000 - 9999 E INTEIRO")
        continue

    tentativas +=1
    tentativas_restantes = max_tentativas - tentativas
    print(f"\nTentativas restantes {tentativas_restantes}")
    print("\n---------------------------------------")

    digito_1 = palpite // 1000     
    digito_2 = (palpite // 100) % 10
    digito_3 = (palpite // 10) % 10  
    digito_4 = palpite % 10 

    cod_secreto_1 = codig_secret // 1000     
    cod_secreto_2 = (codig_secret // 100) % 10
    cod_secreto_3 = (codig_secret // 10) % 10  
    cod_secreto_4 = codig_secret % 10 

    if digito_1 == cod_secreto_1:
        prog_digito_1 = digito_1
        #posicao += 1

    else: 
        digito_1 != cod_secreto_1
        #posicao += 1

    if digito_2 == cod_secreto_2:
        prog_digito_2 = digito_2
        #posicao += 1

    else:
        digito_2 != cod_secreto_2
        #posicao += 1

    if digito_3 == cod_secreto_3:
        prog_digito_3 = digito_3
        #posicao += 1

    else:
        digito_3 != cod_secreto_3
        #posicao += 1

    if digito_4 == cod_secreto_4:
        prog_digito_4 = digito_4
        #posicao += 1

    else:
        digito_4 != cod_secreto_4
        #posicao += 1

    #print("\nNúmeros corretos na posição certa:", posicao)
    #print("\nNúmeros corretos na posição errada:", acertos - posicao)

    if prog_digito_1 or prog_digito_2 or prog_digito_3 or prog_digito_4 == codig_secret:
        print(f"\nSeu código é: {prog_digito_1} {prog_digito_2} {prog_digito_3} {prog_digito_4}")
        print("\nVocê acertou 1 dígito(s)!")
    else:
        print("\nVocê não acertou nenhum dígito.")
           
# Dicas a partir da 5ª tentativa
    if tentativas >= 5:
        if prog_digito_1 == -1:
            if digito_1 >= 5:
                print("\n(DICA: O número na posição 1 é maior ou igual a 5)")
            else:
                print("\n(DICA: O número na posição 1 é menor que 5)")
        elif prog_digito_2 == -1:
            if digito_2 >= 5:
                print("\n(DICA: O número na posição 2 é maior ou igual a 5)")
            else:
                print("\n(DICA: O número na posição 2 é menor que 5)")
        elif prog_digito_3 == -1:
            if digito_3 >= 5:
                print("\n(DICA: O número na posição 3 é maior ou igual a 5)")
            else:
                print("\n(DICA: O número na posição 3 é menor que 5)")
        elif prog_digito_4 == -1:
            if digito_4 >= 5:
                print("\n(DICA: O número na posição 4 é maior ou igual a 5)")
            else:
                print("\n(DICA: O número na posição 4 é menor que 5)")