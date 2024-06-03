import os
from Menu import Menu
from Manejador import ManejadorViajero


if __name__ == "__main__":
    os.system("cls")
    manViajero = ManejadorViajero()
    manViajero.test()
    manViajero.cargarViajero()
    
    manViajero.compararSobrecargar()
    manViajero.acumularSobrecargarReverso()
    manViajero.canjearSobrecargaReverso()