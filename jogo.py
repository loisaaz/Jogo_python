print("BEM VINDO AO JOGO SECRETO!! ")


print("O objetivo é acertar o número secreto. ")
print("Você 10 tentativas para acertar o número secreto entre [1000 e 9999]")
print("A partir da 5° tentativa o jogo irá te ajudar com  dicas ")
print("\n>>>TECLE ALGO PARA CONTINUAR <<<<: ")

import random 
codig_secret= random.randint(1000,9999)
palpitec=int(input("digite um número com 4 dígitos:"))
