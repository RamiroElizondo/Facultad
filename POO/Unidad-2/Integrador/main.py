from ManejadorCama import ManejadorCama
from ManejadorMedicamento import ManejadorMedicamento


if __name__ == '__main__':
    manejadorC = ManejadorCama()
    manejadorM = ManejadorMedicamento()
    manejadorM.CargaM()
    nombre = input('Ingrese Nombre Y Apellido de un paciente: ')
    valorcama = manejadorC.buscarMostrar(nombre)
    manejadorM.mostrar(valorcama)
    diagnostico = input('Ingrese diagnostico: ')
    manejadorC.listar(diagnostico)
"""
Venerdini,Analia
22/09/29
"""