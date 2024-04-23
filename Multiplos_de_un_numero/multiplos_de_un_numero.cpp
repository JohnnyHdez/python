#include <iostream>
#include <stdio.h>

using namespace std;

/*
Compilador: Dev-C++ 5.11
author: Johnny Hernández
fecha: 24 de febrero de 2023
*/
void function(int, int);

int main(int argc, char** argv){
	
	system("cls");
	
	int numero = 0;
	int elementos = 0;
	
	cout << "Este programa genera un arreglo de multiplos de un n\xA3mero" << endl;
	
	cout << "Ingresar n\xA3mero: ";
	cin >> numero;
	
	cout << "Ingresar cantidad de elementos: ";
	cin >> elementos;
	
	function(numero, elementos);
	
	system("pause");
	
	return 0;
}

void function(int numero, int elementos){
	
	int array[elementos];
	
	for(int i = 0; i < elementos; i++){
		array[i] = numero * (i + 1);
	}
	cout << "Arreglo de multiplos de " << numero << " es ";
	for (int j = 0; j < elementos; j++){
		cout << array[j] << " ";
	}
	cout << endl;
}

