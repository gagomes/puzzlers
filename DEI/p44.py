#!/usr/bin/python

"""
Sequencia Recursiva   

Pretende-se que elabore um programa recursivo que le um numero N (maior que 0)
do utilizador e imprima a sequencia descendente e ascendente dos numeros que
lhe sao inferiores.

O output devera corresponder a sequencia descendente a partir de N ate 1,
depois a sequencia ascendente a partir de 2 ate N.
Por exemplo para N = 8, devera imprimir: 

"8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 "

Nota: Para facilitar o problema, o ultimo numero tambem leva um espaco a 
direita.
"""

def recf(n):
    if n == 1:
        return "1 "
    return str(n) + " " + recf(n-1) + str(n) + " "

print recf(int(input()))

