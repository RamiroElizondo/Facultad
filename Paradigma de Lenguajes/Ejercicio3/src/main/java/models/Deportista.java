/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package models;

/**
 *
 * @author ramir
 */
public class Deportista {
    private String nombre;
    private String dni;
    private Integer numeroJugador;
    
    public Deportista(String nombre,String dni){
        this.nombre = nombre;
        this.dni = dni;
        this.numeroJugador = 0;
    }
    
    public String getNombre(){
        return nombre;
    }
    public String getDNI(){
        return dni;
    }
    public Integer getNumero(){
        return numeroJugador;
    }
    public void setNombre(String nom){
        this.nombre = nom;
    }
    public void setDNI(String dni){
        this.dni = dni;
    }
    public void setNumero(Integer num){
        this.numeroJugador = num;
    }
    public String toString(){
        return "Deportista: "+nombre+" DNI: "+dni+" Numero: "+numeroJugador;
    }
    
}

