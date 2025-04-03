print("\nBEM VINDO AO JOGO SECRETO!!")
print("\nO objetivo é acertar o número secreto.")
print("\nVocê 10 tentativas para acertar o número secreto entre [1000 e 9999]")
print("\nA partir da 5° tentativa o jogo irá te ajudar com  dicas")
print("\n>>>TECLE ALGO PARA CONTINUAR <<<<:")
input() # tecle algo para aparecer a próxima tela

import random 
codig_secret= random.randint(1000,9999) #biblioteca
palpite=int(input("Digite um número com 4 dígitos:"))

# separar dígitos para comparação
digito_1 = palpite // 1000     
digito_2 = (palpite // 100) % 10
digito_3 = (palpite // 10) % 10  
digito_4 = palpite % 10 
print(digito_1)
print(digito_2)
print(digito_3)
print(digito_4)


# separar digitos codigo secreto
cod_secreto_1 = codig_secret // 1000     
cod_secreto_2 = (codig_secret // 100) % 10
cod_secreto_3 = (codig_secret // 10) % 10  
cod_secreto_4 = codig_secret % 10 

print(cod_secreto_1)
print(cod_secreto_2)
print(cod_secreto_3)
print(cod_secreto_4)

# adicionar um loop para comparaçao entre o palpite e o cod secreto (for ou while)
# criar variáveis para contar (logo entendemos que precisamos adicionar um contador) quantos dígitos estão corretos (se correto deve aparecer) e quantos estão na posição certa.
# loop para contagem de tentativas