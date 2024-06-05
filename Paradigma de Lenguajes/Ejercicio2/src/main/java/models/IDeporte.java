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
public interface IDeporte {
    public Integer CANTIDAD_MINIMA=2;
    public boolean conformar(List<Deportista>datos);
    public void mostrar();
    public void numerarDeportista();
}
