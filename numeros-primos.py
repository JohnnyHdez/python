#-encoding: utf8
def primos(*lista):
    mult = 0 #Cantidad de multiplos de un numero
    lista_init = list(lista) #Lista de numeros iniciales
    primos_lista = []
    if len(lista_init) == 0:
        print('Por favor digite una lista de números para determinar si son números primos')
    else:
        for n in lista_init:
            mult = 0 #Hay que inicializar en cero para cada valor de la lista
            for i in range(1, n+1): #hay que sumar uno al número para que sea inclusive
                if n % i == 0: #si esta condicion se da hemos hallado un multiplo
                    mult += 1
            if mult == 2:
                #los númmros primos sólo tiene dos multiplos
                primos_lista.append(n)
                

    if len(primos_lista) > 0:
        print('Estos son los números primos')
    else:
        print('No hay números primos en estos valores')
    return primos_lista

resultado = primos(1,2,3,4,5,6,7,8,9,10)
print(resultado)

