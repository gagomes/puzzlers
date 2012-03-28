#!/usr/bin/python

"""
Deves construir um programa que leia 3 pares de números e imprima para cada para cada um dos pares a soma destes utilizando o inverso dos números. O que é o inverso dos números? Se o número for 1234, o seu inverso é 4321.

Por exemplo, dado o par 4358 e 754 deverás imprimir 1998 porque 4358 + 754 = 8534 + 457 = 8991 = 1998.

Os pares são dados na mesma linha separados por um espaço.
"""

for _ in range(3):
  s = raw_input()
  l = s.split(' ')
  n = 0
  for num in l:
    n += int(num[::-1])
  print str(n)[::-1]
