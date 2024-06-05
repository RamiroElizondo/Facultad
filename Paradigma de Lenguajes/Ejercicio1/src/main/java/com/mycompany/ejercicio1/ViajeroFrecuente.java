/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicio1;

public class ViajeroFrecuente {
    private Integer numero;
    private String dni;
    private String nombre;
    private String apellido;
    private Integer millas;
    public ViajeroFrecuente(Integer numero,String dni,String nombre,String apellido,Integer millas){
        this.numero = numero;
        this.dni = dni;
        this.nombre = nombre;
        this.apellido = apellido;
        this.millas = millas;
    }
    public Integer getNumero(){
        return numero;
    }
    public String getDni(){
        return dni;
    }
    public String getNombre(){
        return nombre;
    }
    public String getApellido(){
        return apellido;
    }
    public Integer getMillas(){
        return millas;
    }
    
    public void setNum(Integer numero){
        this.numero = numero;
    }
    public void setDni(String dni){
        this.dni = dni;
    }
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    public void setApellido(String apellido){
        this.apellido = apellido;
    }
    public void setMillas(Integer millas){
        this.millas = millas;
    }
    
    @Override
    public String toString(){
        return "Viajero:" + " DNI: "+dni+" Nombre y Apellido: "+nombre + " " + apellido+" Milas: "+millas;
    }
}
