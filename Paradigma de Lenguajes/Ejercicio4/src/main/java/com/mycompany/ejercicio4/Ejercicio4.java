/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.ejercicio4;
import java.util.Scanner;
/**
 *
 * @author ramir
 */


public class Ejercicio4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Gestor gestor = new Gestor(10);
        String opcion = "";
        while (!opcion.equals("g")){
            System.out.println("a- Cargar Viajero");
            System.out.println("b- Mostrar Viajero de forma ordenada por millas");
            System.out.println("c- Mostrar viajeros que tienen mas de 200 millas");
            System.out.println("d- Mejor Viajero");
            System.out.println("g- Fin");
            System.out.println("Tu opcion: ");
            opcion = scanner.nextLine();
            switch (opcion) {
                case "a" -> gestor.CargarViajero();
                case "b" -> gestor.MostrarOrdenado();
                case "c" -> gestor.MostrarMayores();
                case "d" -> gestor.MejorViajero();
                default -> System.out.println("Opcion Incorrecta");
            }
        }
        scanner.close();
    }
}

