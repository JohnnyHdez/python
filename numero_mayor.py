#!/usr/bin/env python
#-*- encoding:utf8 -*-

'''
Compilador: Python 3.10.4
author: Johnny Hernandez
fecha: 02 de abril de 2023
'''

class NumeroLimite:
    def __init__(self, lista_numero:str):
        self.numeros = lista_numero
        
    def listaOrdenada(self):
        listai = list(self.numeros.split(","))
        listao = list(map(int, listai))
        listao.sort()
        return listao
    
    def numeroMayor(self):
        '''
        Se crea  una lista con los numeros de tipo string

        Ejemplo "5" int("5") = 5
        '''
        mi_lista_de_numeros = list(self.numeros.split(","))
        i = 1

        '''
        Asumo que el primer número de la lista es el mayor
        Como es un string lo convierto a número entero
        '''
        numero_mayor = int(mi_lista_de_numeros[0])
        
        while i < len(mi_lista_de_numeros):
            if int(mi_lista_de_numeros[i]) > numero_mayor:
                numero_mayor = int(mi_lista_de_numeros[i])
            i += 1
        return numero_mayor

    def numeroMenor(self):
        '''
        Se crea  una lista con los numeros de tipo string

        Ejemplo "5" int("5") = 5
        '''
        mi_lista_de_numeros = list(self.numeros.split(","))
        i = 1

        '''
        Asumo que el primer número de la lista es el menor
        Como es un string lo convierto a número entero
        '''
        numero_menor = int(mi_lista_de_numeros[0])
        
        while i < len(mi_lista_de_numeros):
            if int(mi_lista_de_numeros[i]) < numero_menor:
                numero_menor = int(mi_lista_de_numeros[i])
            i += 1
        return numero_menor
    
    def numeroMedio(self):
        numero_medio = 0

        mi_lista = self.listaOrdenada()
        cantidad_elementos = len(mi_lista)

        if cantidad_elementos % 2 != 0:
            numero_medio = mi_lista[cantidad_elementos//2]
        elif cantidad_elementos % 2 == 0:
            rangoi = (cantidad_elementos//2) - 1
            rangof = cantidad_elementos//2
            numero_medio = (mi_lista[rangoi] + mi_lista[rangof]) / 2

        return numero_medio

if __name__ == "__main__":
    lista_de_numeros = input("Lista de numeros separados por coma: ")
    mi_numero_limite = NumeroLimite(lista_de_numeros)
    
    numero_mayor = mi_numero_limite.numeroMayor()
    print("Número mayor: {}".format(numero_mayor))

    numero_menor = mi_numero_limite.numeroMenor()
    print("Número menor: {}".format(numero_menor))

    numero_medio = mi_numero_limite.numeroMedio()
    print("Número medio: {}".format(numero_medio))
