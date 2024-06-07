/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicio4;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;
import static java.util.Comparator.comparing;
import java.util.Optional;


public class Gestor {
    private final Scanner scanner;
    private final Integer cantidad;
    private final List<ViajeroFrecuente> lista;
    
    public Gestor(Integer cantidad){
        this.cantidad = cantidad;
        this.lista = new ArrayList<>();
        this.scanner = new Scanner(System.in);
    }
    public void CargarViajero(){
        String dni, nom, ape;
        Integer num, milla;
        System.out.println("Datos Viajero");
        System.out.println("Numero: ");
        num = scanner.nextInt();
        scanner.nextLine();
        System.out.println("DNI: ");
        dni = scanner.nextLine();
        System.out.println("Nombre: ");
        nom = scanner.nextLine();
        System.out.println("Apellido: ");
        ape = scanner.nextLine();
        System.out.println("Millas: ");
        milla = scanner.nextInt();
        scanner.nextLine();
        ViajeroFrecuente viajero = new ViajeroFrecuente(num,dni,nom,ape,milla);
        long count = lista.stream().count();
        if (count < cantidad){
            lista.add(viajero);
        }else{
            System.out.println("Arreglo Lleno");
        }
    }
    public void MostrarOrdenado(){
        lista.stream()
            .sorted(comparing(ViajeroFrecuente::getMillas))
            .forEach(System.out::println);
    }
    public void MostrarMayores(){
        lista.stream()
            .filter(v->v.getMillas() > 200)
            .forEach(System.out::println);
    }
    
    public void MejorViajero(){
        Optional<ViajeroFrecuente> v = lista.stream()
                                            .max(comparing(ViajeroFrecuente::getMillas));
        v.ifPresentOrElse(
                viajero-> System.out.println("El viajero con mas millas es: "+v),
                () -> System.out.println("No hay viajero")
        );   
    }
}