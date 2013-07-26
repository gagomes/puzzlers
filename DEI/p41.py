#!/usr/bin/python

"""
Soma de ímpares   [ 280 pontos ] 

Dada uma gama de valores [a, b], deves procurar a soma de todos os inteiros 
ímpares que fazem parte dessa gama. Por exemplo, a soma de todos os inteiros 
ímpares da gama [3, 9] é 3 + 5 + 7 + 9 = 24.

O programa deverá ler duas linhas com o valor a e b e imprimir a soma.
"""

print sum(filter(lambda x: x & 1, range(int(raw_input()), int(raw_input()) + 1)))
