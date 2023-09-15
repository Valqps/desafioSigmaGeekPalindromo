from mpmath import mp
import math


def primo(n):
    m = 0
    final = int(math.sqrt(n))
    for j in range(2, final):
        if n % j == 0:
            m = 1
    if m == 0:
        return 1
    else:
        return 0


mp.dps = 10
indice = 0
numero = 0
numeroint = 0
a = 0
resposta = 0
palindromo = 0
pi = str(mp.pi)

while resposta == 0:
    mp.dps *= 10
    pi = str(mp.pi)
    while indice < len(pi) - 8 and resposta != 1:
        # Laço para avaliar se é palíndromo
        while a < 4:
            if pi[indice + a] == pi[indice + 8 - a]:
                a += 1
                if a == 4:
                    palindromo = 1
                    numero = pi[indice:(indice + 9)]
                    print(indice)
                    print(numero)
                    for k in range(0, 9):
                        numeroint = numeroint + eval(numero[k]) * 10 ** (8 - k)
                        # se chegar aqui, é palíndromo
                    print(numeroint)
                    resposta = primo(numeroint)
                    numeroint = 0
            else:
                a = 5
                # sair do laço do a e aumentar o índice
        a = 0
        indice += 1
print("fim")