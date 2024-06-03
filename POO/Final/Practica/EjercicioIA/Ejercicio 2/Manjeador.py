from ClaseVehiculo import Vehiculo
from ClaseCamioneta import Camioneta
from ClaseAuto import Auto
from ClaseConcesionario import Concesionario

class Manejador:
    __listaCon:list[Concesionario]

    def __init__(self):
        self.__listaCon = []
    
    def crearCon(self):
        nombre = input('Ingrese nombre: ')
        con = Concesionario(nombre)
        self.__listaCon.append(con)
        self.agregar(con)

    def agregar(self,con):
        cant = int(input('Cuantos vehiculos quieres agregar: '))
        for i in range(0,cant):
            marca = input('Ingrese marca: ')
            modelo = input('Ingrese modelo: ')
            año = input('Ingrese año: ')
            variable = input('Auto o Camioneta: ')
            if variable == 'Auto':
                puerta = input('Ingrese puertas: ')
                objeto = Auto(marca, modelo, año, puertas)
                con.agregarVehiculo(objeto)
            if variable == 'Camioneta':
                carga = input('Ingrese carga: ')
                objeto = Camioneta(marca,modelo,año,carga)
                con.agregarVehiculo(objeto)
        
    def mostrar(self):
        for con in self.__listaCon:
            for objeto in con.listarVehiculo():
                print(objeto.obtenerInformacion())