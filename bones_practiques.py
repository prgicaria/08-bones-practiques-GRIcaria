#!/usr/bin/env python

'''Divisió entera. Calcula la divisió entre dos nombres

Institut Icària
Programació - 1r Batxillerat - Curs 2023-24

Demana dos nombres enters, mostra la divisió el resultat
en nombre enter i el residu
'''
__author__ = "Gabriel Rodríguez"
__contact__ = "grvalenzuelay@instituticaria.cat"
__date__ = "2024/10/06"

dividend = int(input("Dividend: "))
divisor = int(input("Divisor: "))
quocient = dividend // divisor
residu = dividend % divisor

print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")
