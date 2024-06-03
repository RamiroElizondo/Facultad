from ObjectEncoder import ObjectEncoder
from ClaseLista import ListaEnlazada
from ClaseHeladera import Heladera
from ClaseLavarropa import Lavarropa
from ClaseTelevisor import Televisor


class Menu:
    __manejador: ObjectEncoder

    def __init__(self):
        self.__lista = ListaEnlazada()
        self.__manejador = ObjectEncoder()
        self.__manejador.cargarObjetos(self.__lista)

    def mostrar(self):
        print('Menu Opciones'.center(30,'-'))
        print('0- Salir')
        print('1- Insertar Aparato')
        print('2- Agregar Aparato')
        print('3- Mostrar Aparato de una posicion')
        print('4- Mostrar Cantidad de cada Aparato')
        print('5- Mostrar Marca de todos los Aparatos')
        print('6- Mostrar Aparatos en venta')
        print('7- Almacenar Objetos')
    
    def crearAparatos(self):
        objeto = None
        tipo = input('Ingrese el tipo de Aparato: ')
        if tipo != 'Heladera' and tipo != 'Lavarropa' and tipo != 'Televisor':
            raise Exception('Tipo de Aparato no valido')
        marca = input('Ingrese la marca: ')
        modelo = input('Ingrese el modelo: ')
        color = input('Ingrese el color: ')
        pais = input('Ingrese el pais: ')
        precio = float(input('Ingrese el precio: '))
        if tipo == 'Heladera':
            capacidad = float(input('Ingrese la capacidad: '))
            freezer = input('Tiene freezer? (Si/No): ') == 'Si'
            cyclica = input('Tiene cyclica? (Si/No): ') == 'Si'
            objeto = Heladera(marca, modelo, color, pais, precio, capacidad, freezer, cyclica)
        elif tipo == 'Lavarropa':
            capacidad = float(input('Ingrese la capacidad: '))
            velocidad = int(input('Ingrese la velocidad: '))
            carga = input('Ingrese la carga: ')
            programas = int(input('Ingrese la cantidad de programas: '))
            objeto = Lavarropa(marca, modelo, color, pais, precio, capacidad, velocidad,programas, carga)
        elif tipo == 'Televisor':
            resolucion = input('Ingrese la resolucion: ')
            sintonizador = input('Tiene sintonizador? (Si/No): ') == 'Si'
            tipoDefinicion = input('Ingrese el tipo de definicion: ')
            internet = input('Tiene internet? (Si/No): ') == 'Si'
            objeto = Televisor(marca, modelo, color, pais, precio, resolucion, sintonizador, tipoDefinicion, internet)
        return objeto

    def opcion1(self):
        posicion = int(input('Ingrese la posicion: '))
        objetoA = self.crearAparatos()
        self.__lista.insertarElemento(objetoA,posicion)

    def opcion2(self):
        objetoA = self.crearAparatos()
        self.__lista.agregarElemento(objetoA)

    def opcion3(self):
        posicion = int(input('Ingrese posicion: '))
        self.__lista.mostrarposicion(posicion)
        self.__lista.mostrarLista()

    def opcion4(self):
        self.__lista.contar()

    def opcion5(self):
        self.__lista.mostrarMarcaLavarropa()

    def opcion6(self):
        self.__lista.mostrarDatosVenta()
    
    def opcion7(self):
        self.__manejador.GuardarJson(self.__lista)

    def menuOpciones(self,opcion):
        if opcion == 1:
            self.opcion1()
        elif opcion == 2:
            self.opcion2()
        elif opcion == 3:
            self.opcion3()
        elif opcion == 4:
            self.opcion4()
        elif opcion == 5:
            self.opcion5()
        elif opcion == 6:
            self.opcion6()
        elif opcion == 7:
            self.opcion7()
        elif opcion != 0 and opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5 and opcion != 6 and opcion != 7:
            print('Opcion Invalida')

