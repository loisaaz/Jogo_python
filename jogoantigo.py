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
progresso = "_ _ _ _"
prog_digito_1 = "_"
prog_digito_2 = "_"
prog_digito_3 = "_"
prog_digito_4 = "_"

while tentativas < max_tentativas:
    palpite = int(input("Digite seu palpite sendo um número de 4 dígitos:"))
    if palpite < 1000 or palpite > 9999 or float:
        print("\nATENÇÃO! ! !")
        print("\nINSIRA UM VALOR NO INTERVALO DE 1000 - 9999 E INTEIRO")
    else:
        palpite = int(input("Digite seu palpite sendo um número de 4 dígitos:"))

    tentativas +=1
    tentativas_restantes = max_tentativas - tentativas
    print(f"\nTentativas restantes {tentativas_restantes}")

    # separar dígitos do palpite
    digito_1 = palpite // 1000     
    digito_2 = (palpite // 100) % 10
    digito_3 = (palpite // 10) % 10  
    digito_4 = palpite % 10 
    #print(digito_1)
    #print(digito_2)
    #print(digito_3)
    #print(digito_4)

    # separar digitos codigo secreto
    cod_secreto_1 = codig_secret // 1000     
    cod_secreto_2 = (codig_secret // 100) % 10
    cod_secreto_3 = (codig_secret // 10) % 10  
    cod_secreto_4 = codig_secret % 10 
    #print(cod_secreto_1)
    #print(cod_secreto_2)
    #print(cod_secreto_3)
    #print(cod_secreto_4)

    #variáveis para contar dígitos corretos/errados.
    digitos_certos = 0
    digitos_errados = 0

    if digito_1 == cod_secreto_1:
        prog_digito_1 = digito_1
        #digitos_certos += 1
        #print("\nVocê acertou 1 dígito(s)!")
    elif digito_1 != cod_secreto_1:
        digitos_errados += 1
        #print("\nVocê não acertou nenhum dígito.")

    if digito_2 == cod_secreto_2:
        #digitos_certos += 1
        prog_digito_2 = digito_2
        #print("\nVocê acertou 1 dígito(s)!")
    elif digito_2 != cod_secreto_2:
        digitos_errados += 1
        #print("\nVocê não acertou nenhum dígito.")

    if digito_3 == cod_secreto_3:
        prog_digito_3 = digito_3
        #digitos_certos += 1
        #print("\nVocê acertou 1 dígito(s)!")
    elif digito_3 != cod_secreto_3:
        digitos_errados += 1
        #print("\nVocê não acertou nenhum dígito.")

    if digito_4 == cod_secreto_4:
        prog_digito_4 = digito_4
        #digitos_certos += 1
        #print("\nVocê acertou 1 dígito(s)!")
    elif digito_4 != cod_secreto_4:
        digitos_errados += 1
        #print("\nVocê não acertou nenhum dígito.")

    print(f"\nSeu código é: {prog_digito_1} {prog_digito_2} {prog_digito_3} {prog_digito_4}")
    if prog_digito_1 or prog_digito_2 or prog_digito_3 or prog_digito_4 == codig_secret:
        print("\nVocê acertou 1 dígito(s)!")
    else:
        print("\nVocê não acertou nenhum dígito.")
#dicas
    if tentativas >= 5:
        if palpite < codig_secret:
            print("DICA: O número secreto é MAIOR que seu palpite.")
        else:
            print("DICA: O número secreto é MENOR que seu palpite.")
    for i in range(4):
        if palpite == codig_secret:
         print(f'\nSEU CÓDIGO É:')
 
    if palpite == codig_secret:
            print("\nPARABÉNS! Você acertou o número secreto!")
            break
    if tentativas == max_tentativas:
            print(f"\nVocê não acertou o número secreto. O número era {codig_secret}.")
