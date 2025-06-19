import random 

print("\n\tBEM VINDO AO JOGO SECRETO!!")
print("\n\tO objetivo é acertar o número secreto.")
print("\n\tVocê 10 tentativas para acertar o número secreto entre [1000 e 9999]")
print("\n\tA partir da 5° tentativa o jogo irá te ajudar com  dicas.")
print("\n\t>>>TECLE ALGO PARA CONTINUAR <<<<")
input()

codig_secret= random.randint(1000,9999) 

tentativas = 0 
max_tentativas = 10

prog_digito_1 = "_"
prog_digito_2 = "_"
prog_digito_3 = "_"
prog_digito_4 = "_"

while tentativas < max_tentativas:
    palpite = int(input("\n\tDigite seu palpite: "))
    while palpite < 1000 or palpite > 9999:
        print("\n\tINSIRA UM VALOR INTEIRO NO INTERVALO DE 1000 - 9999")
        palpite = int(input("\n\tDigite seu palpite : "))    

    print("\n--------------------------------------------------------------")

    tentativas +=1
    tentativas_restantes = max_tentativas - tentativas
    print(f"\n\tTentativas restantes: {tentativas_restantes}")

    print("\n--------------------------------------------------------------")

    digito_1 = palpite // 1000     
    digito_2 = (palpite // 100) % 10
    digito_3 = (palpite // 10) % 10  
    digito_4 = palpite % 10 

    cod_secreto_1 = codig_secret // 1000     
    cod_secreto_2 = (codig_secret // 100) % 10
    cod_secreto_3 = (codig_secret // 10) % 10  
    cod_secreto_4 = codig_secret % 10 

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

    print(f"\n\tSEU CÓDIGO É: {prog_digito_1} {prog_digito_2} {prog_digito_3} {prog_digito_4}")


    if prog_digito_1 != "_" and prog_digito_2 != "_" and prog_digito_3 != "_" and prog_digito_4 != "_":
        print("\n--------------------------------------------------------------")
        print("\nP A R A B É N S ! ! ! \tVOCÊ DESCOBRIU TODOS OS DÍGITOS CORRETOS!")
        print(f"\nO CÓDIGO SECRETO ERA: {codig_secret}")
        jogar_novamente = int(input("\nDeseja jogar novamente? (1 = SIM / 0 = NÃO): "))
        if jogar_novamente == 1:
            codig_secret = random.randint(1000, 9999)
            tentativas = 0
            prog_digito_1 = prog_digito_2 = prog_digito_3 = prog_digito_4 = "_"
        else:
            print("\nObrigado por jogar!")

    print("\n--------------------------------------------------------------")    

    if tentativas_restantes == 5:
        print("\n\tVou te ajudar com dicas! ")

        if prog_digito_1 != "_":
            print(f"{prog_digito_1}", end=" ")
        else:
            if cod_secreto_1 % 2 == 0:
                print("PAR", end=" ")
            else:
                print("ÍMPAR", end=" ")
        if prog_digito_2 != "_":
            print(f"{prog_digito_2}", end=" ")
        else:
            if cod_secreto_2 % 2 != 0:
                print("ÍMPAR", end=" ")
            else:
                print("ÍMPAR", end=" ")
        if prog_digito_3 != "_":
            print(f"{prog_digito_3}", end=" ")
        else:
            if cod_secreto_3 % 2 == 0:
                print("PAR", end=" ")
            else:
                print("ÍMPAR", end=" ")
        if prog_digito_4 != "_":
            print(f"{prog_digito_4}", end=" ")
        else:
            if cod_secreto_4 % 2 != 0:
                print("ÍMPAR", end=" ")
            else:
                print("ÍMPAR", end=" ")
        print()

    if tentativas_restantes == 4:
        if codig_secret > palpite:
            print(f"\nDica: O número secreto está acima de {palpite}!")
        else:
            print(f"\nDica: O número secreto está abaixo de {palpite}!")


    if tentativas_restantes == 3:
        if cod_secreto_1 == cod_secreto_4:
            print("\nDica: O primeiro e o último dígito do número secreto são iguais!")

    if tentativas_restantes == 0 and palpite != codig_secret:
        print("\n--------------------------------------------------------------")
        print(f"\nVOCÊ NÃO ACERTOU O NÚMERO SECRETO, O CÓDIGO ERA: {codig_secret}") 
        jogar_novamente = int(input("\nDeseja jogar novamente? (1 = SIM / 0 = NÃO): "))
        if jogar_novamente == 1:
            codig_secret = random.randint(1000, 9999)
            tentativas = 0
            prog_digito_1 = prog_digito_2 = prog_digito_3 = prog_digito_4 = "_"
        else:
            print("\nObrigado por jogar!")