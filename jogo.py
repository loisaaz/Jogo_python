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

while tentativas < max_tentativas:
    palpite = int(input("Digite seu palpite sendo um número de 4 dígitos:"))
    if palpite < 1000 or palpite > 9999:
        print("\nATENÇÃO! ! !")
        print("\nINSIRA UM VALOR NO INTERVALO DE 1000 E 9999")
        continue

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

# escolhi usar elif porque estamos trabalhando com bastantes possibilidades e ele facilita mais que o else.
# as listas tornam o trabalho mais fácil caso algo precise ser alterado e o código fica mais limpo 
# especialmente quando há múltiplas verificações. 

    if digito_1 == cod_secreto_1:
        digitos_certos += 1
        print("\nVocê acertou 1 dígito(s)!")
    elif digito_1 in [cod_secreto_2, cod_secreto_3, cod_secreto_4]:
        digitos_errados += 1
        print("\nVocê não acertou nenhum dígito.")

    if digito_2 == cod_secreto_2:
        digitos_certos += 1
        print("\nVocê acertou 1 dígito(s)!")
    elif digito_2 in [cod_secreto_1, cod_secreto_3, cod_secreto_4]:
        digitos_errados += 1
        print("\nVocê não acertou nenhum dígito.")

    if digito_3 == cod_secreto_3:
        digitos_certos += 1
        print("\nVocê acertou 1 dígito(s)!")
    elif digito_3 in [cod_secreto_1, cod_secreto_2, cod_secreto_4]:
        digitos_errados += 1
        print("\nVocê não acertou nenhum dígito.")

    if digito_4 == cod_secreto_4:
        digitos_certos += 1
        print("\nVocê acertou 1 dígito(s)!")
    elif digito_4 in [cod_secreto_1, cod_secreto_2, cod_secreto_3]:
        digitos_errados += 1
        print("\nVocê não acertou nenhum dígito.")

    if tentativas == max_tentativas:
        print(f"\nVocê não acertou o número secreto. O número era {codig_secret}.")
  
# print("\nSeu dígito é:")


