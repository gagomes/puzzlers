#!/usr/bin/python

"""
Física do Secundário   [ 250 pontos ] 

Uma partícula tem velocidade inicial e aceleração constante. Se a sua
velocidade após uma certa quantidade de tempo é v, então qual será o seu
deslocamento no dobro desse tempo?

Escreve um programa que lê do utilizador uma linha com dois números v (-100 <=
v <= 100) e t (0<=t<= 200) (t corresponde ao tempo que a partícula ganhou a tal
velocidade v).
O programa deve imprimir um único valor inteiro correspondendo ao deslocamento
no dobro do tempo t.
"""


import sys

v, t = map(int, raw_input().split())
if not ((v >= -100 and v <= 100) or (t >= 0 and t <= 200)):
    sys.exit(1)

print int(v * (t * 2))
