print("\nBEM VINDO AO JOGO SECRETO!!")
print("\nO objetivo é acertar o número secreto.")
print("\nVocê tem 10 tentativas para acertar o número secreto entre [1000 e 9999]")
print("\nA partir da 5ª tentativa, o jogo irá te ajudar com dicas.")
print("\n>>> TECLE ALGO PARA CONTINUAR <<<:")
input()

import random 
codig_secret = random.randint(1000, 9999) 

tentativas = 0 
max_tentativas = 10
acertos = 0
prog_digito = ["_", "_", "_", "_"] 

while tentativas < max_tentativas:
    print("\n---------------------------------------")
    palpite = int(input("Digite seu palpite sendo um número de 4 dígitos: "))
    
    if palpite < 1000 or palpite > 9999:
        print("\nATENÇÃO! ! !")
        print("\nINSIRA UM VALOR NO INTERVALO DE 1000 - 9999 E INTEIRO")
        break

    tentativas += 1
    tentativas_restantes = max_tentativas - tentativas
    print(f"\nTentativas restantes: {tentativas_restantes}")
    print("\n---------------------------------------")

    digitos_palpite = [palpite // 1000, (palpite // 100) % 10, (palpite // 10) % 10, palpite % 10]
    digitos_secreto = [codig_secret // 1000, (codig_secret // 100) % 10, (codig_secret // 10) % 10, codig_secret % 10]

    posicao = 0
    acertos = 0

    for i in range(4):
        if digitos_palpite[i] == digitos_secreto[i]:
            prog_digito[i] = digitos_palpite[i]
            posicao += 1
        elif digitos_palpite[i] in digitos_secreto:
            acertos += 1

    print("\nNúmeros corretos na posição certa:", posicao)
    print("Números corretos na posição errada:", acertos)

    # Exibe o progresso dos dígitos corretos
    print("\nSeu código é:", prog_digito[0], prog_digito[1], prog_digito[2], prog_digito[3])

    if palpite == codig_secret:
        print("\nPARABÉNS! Você acertou o número secreto!")
        break

    if tentativas >= 5:
        if palpite < codig_secret:
            print("DICA: O número secreto é MAIOR que seu palpite.")
        else:
            print("DICA: O número secreto é MENOR que seu palpite.")

    if tentativas == max_tentativas:
        print(f"\nVocê não acertou o número secreto. O número era {codig_secret}.")
