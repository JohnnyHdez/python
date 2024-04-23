package multiplos_de_un_numero;

import java.util.Arrays;
import java.util.Scanner;

/**
Compilador: Java SE 18.0.2
author: Johnny Hernandez
fecha: 24 de febrero de 2023
*/

public class MultiplosDeUnNumero {

	private int[] function(int numero, int elementos){
		int array[] = new int[elementos];

		for (int x = 0; x < elementos ; x++ ) {
			array[x] = numero * (x + 1);
		}
		return array;
	}

	public static void main(String[] args) {
		MultiplosDeUnNumero myArray = new MultiplosDeUnNumero();

		int numero;
		int elementos;

		Scanner keyboard = new Scanner(System.in);

		System.out.println("Este programa genera un arreglo de multiplos de un numero");

		System.out.print("Ingresar numero: ");
		numero = keyboard.nextInt();
		System.out.print("Ingresar cantidad de elementos: ");
		elementos = keyboard.nextInt();

		System.out.print("Arreglo de multiplos de " + numero + " es " +
                Arrays.toString(myArray.function(numero, elementos)));
	}
}
