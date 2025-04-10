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
        print("\nVocê acertou o dígito da casa de milhares!")

    else: 
        digito_1 != cod_secreto_1
        print("\nVocê não acertou o dígito da casa de milhares.")

    if digito_2 == cod_secreto_2:
        prog_digito_2 = digito_2
        print("\nVocê acertou o dígito da casa das centenas!")

    else:
        digito_2 != cod_secreto_2
        print("\nVocê não acertou o dígito da casa das centenas.")

    if digito_3 == cod_secreto_3:
        prog_digito_3 = digito_3
        print("\nVocê acertou o dígito da casa das dezenas!")

    else:
        digito_3 != cod_secreto_3
        print("\nVocê não acertou o dígito da casa das dezenas.")

    if digito_4 == cod_secreto_4:
        prog_digito_4 = digito_4
        print("\nVocê acertou o dígito da casa das unidades!")

    else:
        digito_4 != cod_secreto_4
        print("\nVocê não acertou o dígito da casa das unidades.")
    #if digito_1 == cod_secreto_1 or digito_2 == cod_secreto_2 or digito_3 == cod_secreto_3 or digito_4 == cod_secreto_4:
        #print(f"\nVocê acertou 1 dígito(s)!")
    #else:
        #print("\nVocê não acertou nenhum dígito.")

    if prog_digito_1 or prog_digito_2 or prog_digito_3 or prog_digito_4 == codig_secret:
        print(f"\nSeu código é: {prog_digito_1} {prog_digito_2} {prog_digito_3} {prog_digito_4}")           

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
        
        if max_tentativas > tentativas:
            print("\n---------------------------------------")
            print(f"\nVOCÊ NÃO ACERTOU O NÚMERO SECRETO, O CÓDIGO ERA: {codig_secret}") 
            jogar_novamente = int(input("\nDeseja jogar novamente? (1 - Sim / 0 - Não): "))

        if palpite == codig_secret:
            print("P A R A B É N S ! ! !")
            print("VOCÊ ACERTOU O CÓDIGO SECRETO ! ! !")
   
