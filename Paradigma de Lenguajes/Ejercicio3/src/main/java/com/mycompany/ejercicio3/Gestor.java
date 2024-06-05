/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicio3;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
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
            int i =0;
            while ((linea=bufferLectura.readLine()) != null) {
             // Sepapar la linea leída con el separador definido previamente
                String[] campos = linea.split(SEPARADOR);
                try{
                    
                    if(campos.length!=2){
                        throw new Excepcion("El DNI del deportista esta vacio2");
                    }
                    System.out.println(i);
                    System.out.println("Campo 0 "+campos[0]);
                    System.out.println("Campo 1 "+campos[1]);
                    i++;
                    if(campos[0].equals("") || campos[0].equals("null")){/*Pregunta si la longitud es igual a 0 es decir esta vacio ese campo*/
                        throw new Excepcion("El nombre del deportista esta vacio");
                    }
                    String hola = "";
                    if(hola.equals("")){
                        System.out.println("Hola "+hola.length()+hola.getClass()+campos[1].getClass());
                    }
                    System.out.println("La longitud de campo 1 es :  "+campos[1].length());
                    if(campos[1].length()==2 || campos[1].equals("null")){ 
                        throw new Excepcion("El DNI del deportista esta vacio");
                    }
                    Deportista d = new Deportista(campos[0],campos[1]);
                    datos.add(d); 
                }catch(Excepcion ex){
                    System.out.println(ex.getMessage());
                }
                       
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
        Iterator<Deportista> iterator = datos.iterator();
        
        while(iterator.hasNext()){
            Deportista dep = iterator.next();
            arreglo.add(dep);
            i++;
            if (i==cantidadJugadores){
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

