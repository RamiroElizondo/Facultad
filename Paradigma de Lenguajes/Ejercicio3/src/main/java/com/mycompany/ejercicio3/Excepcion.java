/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicio3;

/**
 *
 * @author ramir
 */
public class Excepcion extends Exception{
    public Excepcion() {
        super();
    }
    public Excepcion(String mensage) {
        super(mensage);
    }
    public Excepcion(String mensage, Throwable causa) {
        super(mensage, causa);
    }
    public Excepcion(Throwable causa) {
        super(causa);
    }
  
}
