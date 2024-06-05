/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicio2;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import models.Deportista;
import models.IDeporte;
import models.Equipo;
import models.Pareja;
/**
 *
 * @author ramir
 */
public class Gestor {
    //Parte del codigo para el metodo main() que debera estar definido en la clase principal.    
    /**
     * @param args the command line arguments
     * @throws java.io.IOException
     */
    
    public static final String SEPARADOR = ",";
    
    public static List<Deportista>leerArchivo(String nombreArchivo)throws IOException{
        BufferedReader bufferLectura = null;
        List<Deportista> datos = new ArrayList<>();
        try {
            bufferLectura = new BufferedReader(new FileReader(nombreArchivo));
            String linea;                  

            while ((linea=bufferLectura.readLine()) != null) {
             // Sepapar la linea leída con el separador definido previamente
             String[] campos = linea.split(SEPARADOR); 
             Deportista d = new Deportista(campos[0],campos[1]);
             datos.add(d);           
            }
        } 
        catch (IOException e) {
            System.out.println(e.getMessage());
        }
        finally {
         // Cierro el buffer de lectura
         if (bufferLectura != null) {
             bufferLectura.close();
         }
        }
        return datos;
    }
    
    /**
    * Crea los equipos con los datos pasados como parámetro
    * @param datos lista con todos los deportistas inscriptos
     * @param cantidadJugadores cantidad de jugadores que conforman un equipo
     * @return una lista de equipos
    */
    public static List<IDeporte> creaEquipos(List<Deportista> datos, int cantidadJugadores){
        int i=0;
        List<IDeporte> equipos = new ArrayList<>();
        List<Deportista> arreglo = new ArrayList<>();
        for(Deportista dep : datos){
            arreglo.add(dep);
            i++;
            if (i==5){
                Equipo equipo= new Equipo();
                equipo.conformar(arreglo);
                equipos.add(equipo);
                arreglo=new ArrayList<>();
                i=0;
            }
        }
        return equipos;
    }
    
    /**
    Crea los equipos con los datos pasados como parámetro
     * @param datos es una lista con todos los deportitas inscriptos
     * @return una lista de Parejas formadas
    */
    public static List<IDeporte> creaParejas(List<Deportista> datos){
        int i = 0;
        List<Deportista> arreglo = new ArrayList<>();
        List<IDeporte> parejas = new ArrayList<>();

        for(Deportista dep:datos){

            arreglo.add(dep);
            i++;
            if(i==2){
                Pareja pareja = new Pareja();
                pareja.conformar(arreglo);
                parejas.add(pareja);
                arreglo=new ArrayList<>();
                i=0;
            }
        }
        return parejas;
    }
    
    /**
    * Numera cada integrante del equipo o de la pareja
     * @param datos 
    */
    public static void numerar(List<IDeporte> datos){
        for(IDeporte dato : datos){
             dato.numerarDeportista();
        }
    }
    /**
    * Muestra los datos de cada equipo o de cada pareja
     * @param datos
    */
    public static void mostrar(List<IDeporte> datos){
          for(IDeporte dato : datos){
              dato.mostrar();
          }
    }
    
      
}

