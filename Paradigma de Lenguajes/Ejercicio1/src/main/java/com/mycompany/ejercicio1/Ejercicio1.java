package com.mycompany.ejercicio1;
import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Gestor gestor = new Gestor(10);
        String opcion = "";
        while (!opcion.equals("Fin")){
            System.out.println("a- Cargar Viajero");
            System.out.println("b- Mostrar Viajero");
            System.out.println("c- Consultar Cantidad de Millas");
            System.out.println("d- Acumular Millas");
            System.out.println("e- Canjear Millas");
            System.out.println("f- Mejor Viajero");
            System.out.println("g- Fin");
            System.out.println("Tu opcion: ");
            opcion = scanner.nextLine();
            if (opcion.equals("a")){
                gestor.CargarViajero();
            }else if(opcion.equals("b")){
                gestor.MostrarViajero();
            }else if(opcion.equals("c")){
                gestor.ConsultarMillas();
            }else if(opcion.equals("d")){
                gestor.AcumularMillas();
            }else if(opcion.equals("e")){
                gestor.CajearMillas();
            }else if(opcion.equals("f")){
                gestor.MejorViajero();
            }else{
                System.out.println("Opcion Incorrecta");
            }
        }
        scanner.close();
    }
}
