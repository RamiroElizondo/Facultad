/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicio1;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Iterator;

public class Gestor {
    private Scanner scanner;
    private Integer cantidad;
    private ArrayList<ViajeroFrecuente> arreglo;
    
    public Gestor(Integer cantidad){
        this.cantidad = cantidad;
        this.arreglo = new ArrayList<>();
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
        if (arreglo.size() < cantidad){
            arreglo.add(viajero);
        }else{
            System.out.println("Arreglo Lleno");
        }
    }
    public void MostrarViajero(){
        Integer num;
        System.out.println("Ingrese numero Viajero: ");
        num = scanner.nextInt();
        scanner.nextLine();
        Iterator<ViajeroFrecuente> iterator = arreglo.iterator();
        while (iterator.hasNext()){
            ViajeroFrecuente viajero = iterator.next();
            if (viajero.getNumero().equals(num)){
                System.out.println(viajero);
            }
        }
    }
    public void ConsultarMillas(){
        String dni;
        boolean band = false;
        System.out.println("Ingrese el DNI Viajero: ");
        dni = scanner.nextLine();
        Iterator<ViajeroFrecuente> iterator = arreglo.iterator();
        while (iterator.hasNext()&& !band){
            ViajeroFrecuente viajero = iterator.next();
            if (viajero.getDni().equals(dni)){
                band = true;
                System.out.println("Su millas son: "+viajero.getMillas());
            }
        }
    }
    public void AcumularMillas(){
        Integer millas,m;
        String dni;
        System.out.println("Ingrese el DNI Viajero: ");
        dni = scanner.nextLine();
        Iterator<ViajeroFrecuente> iterator = arreglo.iterator();
        while(iterator.hasNext()){
            ViajeroFrecuente viajero = iterator.next();
            if(viajero.getDni().equals(dni)){
                System.out.println("Viajero Encontrado, ingrese cantidad Millas: ");
                millas = scanner.nextInt();
                scanner.nextLine();
                m = viajero.getMillas();
                viajero.setMillas(m+millas);
                System.out.println("Millas Acumuladas");
                System.out.println(viajero);
            }
        }
    }
    
    public void CajearMillas(){
        String dni;
        Integer m,millas;
        System.out.println("Ingrese DNI: ");
        dni = scanner.nextLine();
        Iterator<ViajeroFrecuente> iterator = arreglo.iterator();
        while(iterator.hasNext()){
            ViajeroFrecuente viajero = iterator.next();
            if(viajero.getDni().equals(dni)){
                m = viajero.getMillas();
                System.out.println("Ingrese Millas a canjear");
                millas = scanner.nextInt();
                scanner.nextLine();
                if(m>millas){
                    viajero.setMillas(m-millas);
                    System.out.println("Millas Canjeadas");
                }else{
                    System.out.println("Millas Insuficientes");
                }
            }
        }
    }
    public void MejorViajero(){
        Integer maximo = 0;
        ArrayList<ViajeroFrecuente> maximos;
        maximos = new ArrayList<>();
        ViajeroFrecuente vmaximo = null;
        Iterator<ViajeroFrecuente> iterator = arreglo.iterator();
        while(iterator.hasNext()){
            ViajeroFrecuente viajero = iterator.next();
            if(viajero.getMillas()>=maximo){
                maximo = viajero.getMillas();
                maximos.add(viajero);
            }
        }
        Iterator<ViajeroFrecuente> iterator1 = maximos.iterator();
        while(iterator1.hasNext()){
            System.out.println(iterator1.next());
        }

    }
}