/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.ejercicio2;


import java.io.IOException;
import java.util.List;
import java.util.Scanner;
import models.Deportista;
import models.IDeporte;

/**
 *
 * @author ramir
 * @throws java.io.IOException
 */
public class Ejercicio2 {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int cantidadJugadoresFutbol= 5;                  
        
        List<Deportista> datosFutbol = Gestor.leerArchivo("./src/main/java/com/mycompany/ejercicio2/inscriptosFutbol.csv");
        List<Deportista> datosPinPon = Gestor.leerArchivo("./src/main/java/com/mycompany/ejercicio2/inscriptosPinPon.csv");

        
        System.out.println(datosFutbol);
        System.out.println(datosPinPon);
        
        List<IDeporte> equipos = Gestor.creaEquipos(datosFutbol,cantidadJugadoresFutbol);
        List<IDeporte> parejas = Gestor.creaParejas(datosPinPon);
        String opcion = "";
        
        while (!opcion.equals("Fin")){
            System.out.println("a-Numerar Deportistas");
            System.out.println("b-Mostrar Equipos");
            System.out.println("c-Mostrar Parejas");
            System.out.println("Tu Opcion:");
            opcion = sc.nextLine();

            if(opcion.equals("a")){
                Gestor.numerar(equipos);
                Gestor.numerar(parejas);
            }else if(opcion.equals("b")){
                Gestor.mostrar(equipos);
            }else if(opcion.equals("c")){
                Gestor.mostrar(parejas);
            }
        }
    }
}
