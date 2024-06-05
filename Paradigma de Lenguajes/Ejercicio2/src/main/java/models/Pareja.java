/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package models;

import java.util.List;

/**
 *
 * @author ramir
 */
public class Pareja implements IDeporte{
    private List<Deportista> integrantes;
    
    public Pareja(){
        this.integrantes = null;
    }
    
    @Override
    public boolean conformar(List<Deportista> datos) {
        boolean band = false;
        if (datos.size() == CANTIDAD_MINIMA){
            this.integrantes = datos;
            band = true;
        }
        return band;
    }

    @Override
    public void mostrar() {
        for(Deportista dep : integrantes){
            System.out.println(dep);
        }
    }

    @Override
    public void numerarDeportista() {
        int i=1;
        for (Deportista dep : integrantes) {
            dep.setNumero(i);
            i++;
        }
    }
}
