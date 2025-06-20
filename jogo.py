import random 
# tela inicial 
print("\n\tBEM VINDO AO JOGO SECRETO!!")
print("\n\tO objetivo é acertar o número secreto.")
print("\n\tVocê 10 tentativas para acertar o número secreto entre [1000 e 9999]")
print("\n\tA partir da 5° tentativa o jogo irá te ajudar com  dicas.")
print("\n\t>>>TECLE ALGO PARA CONTINUAR <<<<")
input()

codig_secret= random.randint(1000,9999) 

# controle das tentativas
tentativas = 0 
max_tentativas = 10

# progresso dos digitos e acertos
prog_digito_1 = "_"
prog_digito_2 = "_"
prog_digito_3 = "_"
prog_digito_4 = "_"

# loop
while tentativas < max_tentativas:
    palpite = int(input("\n\tDigite seu palpite: "))
    while palpite < 1000 or palpite > 9999:
        print("\n\tINSIRA UM VALOR INTEIRO NO INTERVALO DE 1000 - 9999")
        palpite = int(input("\n\tDigite seu palpite: "))    

    print("\n--------------------------------------------------------------")

    tentativas +=1
    tentativas_restantes = max_tentativas - tentativas
    print(f"\n\tTentativas restantes: {tentativas_restantes}")

    print("\n--------------------------------------------------------------")

    # separar os dígitos do palpite
    digito_1 = palpite // 1000     
    digito_2 = (palpite // 100) % 10
    digito_3 = (palpite // 10) % 10  
    digito_4 = palpite % 10 

    # separar os dígitos do código secreto
    cod_secreto_1 = codig_secret // 1000     
    cod_secreto_2 = (codig_secret // 100) % 10
    cod_secreto_3 = (codig_secret // 10) % 10  
    cod_secreto_4 = codig_secret % 10 

    # compara o palpite com o código secreto
    acertos = 0

    if digito_1 == cod_secreto_1:
        prog_digito_1 = digito_1
        acertos += 1
    if digito_2 == cod_secreto_2:
        prog_digito_2 = digito_2
        acertos += 1
    if digito_3 == cod_secreto_3:
        prog_digito_3 = digito_3
        acertos += 1
    if digito_4 == cod_secreto_4:
        prog_digito_4 = digito_4
        acertos += 1
    if acertos == 0:
        print("\n\tVocê não acertou nenhum número.")

    # mostra os acertos e quais ainda faltam descobrir
    print(f"\n\tSeu código é: {prog_digito_1} {prog_digito_2} {prog_digito_3} {prog_digito_4}")

    # se todos os números forem descobertos
    if prog_digito_1 != "_" and prog_digito_2 != "_" and prog_digito_3 != "_" and prog_digito_4 != "_":
        print("\n--------------------------------------------------------------")
        print("\n\tP A R A B É N S ! ! ! \tVOCÊ DESCOBRIU TODOS OS DÍGITOS CORRETOS!")
        print(f"\n\tO código secreto era: {codig_secret}")
        jogar_novamente = int(input("\n\tDeseja jogar novamente? (1 = SIM / 0 = NÃO): "))
        if jogar_novamente == 1:
            codig_secret = random.randint(1000, 9999)
            tentativas = 0
            prog_digito_1 = prog_digito_2 = prog_digito_3 = prog_digito_4 = "_"
        else:
            print("\n\tObrigado por jogar!")
            break

    print("\n--------------------------------------------------------------")    

    # o jogo fornece dicas a partir da 5º tentativa
    if tentativas_restantes == 5:
        print("\n\tVou te ajudar com dicas! ")

        if prog_digito_1 != "_":
            print(f"\t{prog_digito_1}", end=" ")
        else:
            if cod_secreto_1 % 2 == 0:
                print("\tPAR", end=" ")
            else:
                print("\tÍMPAR", end=" ")

        if prog_digito_2 != "_":
            print(f"\t{prog_digito_2}", end=" ")
        else:
            if cod_secreto_2 % 2 != 0:
                print("\tÍMPAR", end=" ")
            else:
                print("\tÍMPAR", end=" ")

        if prog_digito_3 != "_":
            print(f"\t{prog_digito_3}", end=" ")
        else:
            if cod_secreto_3 % 2 == 0:
                print("\tPAR", end=" ")
            else:
                print("\tÍMPAR", end=" ")

        if prog_digito_4 != "_":
            print(f"\t{prog_digito_4}", end=" ")
        else:
            if cod_secreto_4 % 2 != 0:
                print("\tÍMPAR", end=" ")
            else:
                print("\tÍMPAR", end=" ")
        print()

    if tentativas_restantes == 4:
        print("\n\tVou te ajudar com mais uma dica! ")

        if codig_secret > palpite:
            print(f"\n\tO número secreto está acima de {palpite}!")
        else:
            print(f"\n\tO número secreto está abaixo de {palpite}!")

    if tentativas_restantes == 3:
        if cod_secreto_1 == cod_secreto_4:
            print("\n\tMais uma dica! ")
            print("\n\tO primeiro e o último dígito do número secreto são iguais!")

    if tentativas_restantes == 0 and palpite != codig_secret:
        print("\n--------------------------------------------------------------")
        print(f"\n\tVOCÊ NÃO ACERTOU O NÚMERO SECRETO, O CÓDIGO ERA: {codig_secret}") 
        jogar_novamente = int(input("\n\tDeseja jogar novamente? (1 = SIM / 0 = NÃO): "))
        if jogar_novamente == 1:
            codig_secret = random.randint(1000, 9999)
            tentativas = 0
            prog_digito_1 = prog_digito_2 = prog_digito_3 = prog_digito_4 = "_"
        else:
            print("\n\tObrigado por jogar!")
            break