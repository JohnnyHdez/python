#!/usr/bin/env python3

'''
Compilador: Python 3.10.4
author: Johnny Hernandez
fecha: 24 de febrero de 2023
'''

def function(numero: int, elementos: int):
	array = []
	for x in range(1, elementos + 1):
		array.append(numero * x)
	return array

def main():
	print("Este programa genera un arreglo de multiplos de un número\n")
	numero = int(input("Ingresar número: "))
	elementos = int(input("Ingresar cantidad de elementos: "))

	print("Arreglo de multiplos de ", numero, " es ", function(numero, elementos))

if __name__ == '__main__':
	main()
