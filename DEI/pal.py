#!/usr/bin/python

"""
Um palíndromo é um número ou palavra que pode ser lida tanto da direita 
para a esquerda como da esquerda para a direita. Por exemplo 12321 têm o 
mesmo valor numérico se for lido das duas formas.

Deves fazer um programa que lê três números (três linhas) e imprima para 
cada um deles os números palíndromos vizinhos (um menor e outro maior 
que o valor dado).

O programa deverá imprimir os dois vizinhos na mesma linha começando 
pelo menor valor.
"""


def ispalindrome(n):
    return n == n[::-1]

for _ in range(3):
    pal = raw_input()
    hi = low = ""
    for i in range(int(pal) - 1, -1, -1):
        if ispalindrome(str(i)):
            low = i
            break
    n = int(pal) + 1
    while n:
        if ispalindrome(str(n)):
            hi = n
            break
        else:
            n += 1


    print "%s %s" % (low, hi)
