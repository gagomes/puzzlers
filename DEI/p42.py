#!/usr/bin/python

"""
Múltiplos de 3 ou 5   [ 320 pontos ]

Se listarmos todos os números naturais abaixo de 10 que são múltiplos de 3 ou
5, temos 3, 5, 6 e 9. A soma destes múltiplos é 23.
Procura a soma de todos os múltiplos de 3 ou 5 abaixo de 1000.
"""

# De notar que este problema resolve-se colocando o número resultante
# deste script e não o código que o gera. O problema não é explicito quanto
# a isto

print sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1000)))
