from ClaseLista import ListaEnlazada
from ClasePersonal import Personal
from ObjectEncoder import ObjectEncoder
from ClaseDocente import Docente
from ClaseInvestigador import Investigacion
from ClaseDocenteInvestigador import DocenteInvestigador
from ClasePersonalApoyo import PersonalApoyo
from ManejadorDirector import ManejadorDirector
from ManejadorTesorero import ManejadorTesorero


class Menu:
    __lista: ListaEnlazada
    __manejador: ObjectEncoder

    def __init__(self):
        self.__lista = ListaEnlazada()
        self.__manejador = ObjectEncoder()
        self.__manejador.cargarObjetos(self.__lista)

    def mostrar(self):
        print('Menu Opciones'.center(30,'-'))
        print('0- Salir')
        print('1- Insertar Agente')
        print('2- Agregar Agente')
        print('3- Mostrar Tipo de agente de una posicion')
        print('4- Generar Listado Ordenado de una carrera')
        print('5- Contar Agentes con cierta area')
        print('6- Generar Listado Ordenado de todos los Agentes')
        print('7- Listado de todos los Docentes Investigadores')
        print('8- Almacenar Agentes en JSON')
        print('9- Autenticar Agente')

    def crearAgente(self):
        objeto=None
        tipo = input('Ingrese el tipo de agente:')
        if tipo != "Docente" and tipo != "Investigador" and tipo !="DocenteInvestigador" and tipo != "PersonalApoyo":
            raise Exception('Tipo de agente no valido')
        dato = {
            'cuil': input('Ingrese el CUIL: '),
            'apellido': input('Ingrese el apellido: '),
            'nombre': input('Ingrese el nombre del agente: '),
            'sueldoB' : float(input('Ingrese el sueldo basico: ')),
            'antiguedad': int(input('Ingrese la antiguedad del agente: '))
        }
        if tipo == "Docente":
            dato['carrera'] = input('Ingrese la carrera del agente: ')
            dato['cargo'] = input('Ingrese el cargo del agente: ')
            dato['catedra'] = input('Ingrese la catedra del agente: ')
            objeto = Docente(dato)
        elif tipo == "Ivestigador":
            dato['areaInvestigacion'] = input('Ingrese el area de investigacion del agente: ')
            dato['tipoInvestigacion'] = input('Ingrese el tipo de investigacion del agente: ')
            objeto = Investigacion(dato)
        elif tipo == "DocenteInvestigador":
            dato['carrera'] = input('Ingrese la carrera del agente: ')
            dato['cargo'] = input('Ingrese el cargo del agente: ')
            dato['catedra'] = input('Ingrese la catedra del agente: ')
            dato['areaInvestigacion'] = input('Ingrese el area de investigacion del agente: ')
            dato['tipoInvestigacion'] = input('Ingrese el tipo de investigacion del agente: ')
            dato['categoria'] = input('Ingrese la categoria del agente: ')
            dato['importe'] = float(input('Ingrese el importe del agente: '))
            objeto = DocenteInvestigador(dato)
        elif tipo == "PersonalApoyo":
            dato['categoria'] = input('Ingrese la categoria del agente: ')
            objeto = PersonalApoyo(dato)
        return objeto

    def opcion1(self):
        posicion = int(input('Ingrese la posicion: '))
        agente = self.crearAgente()
        self.__lista.insertarElemento(agente,posicion)
        self.__lista.mostrarLista()

    def opcion2(self):
        agente = self.crearAgente()
        self.__lista.agregarElemento(agente)

    def opcion3(self):
        posicion = int(input('Ingrese la posicion: '))
        self.__lista.mostrarElemento(posicion)

    def opcion4(self):
        nomCarrera = input('Ingrese el nombre de la carrera: ')
        lista:list[DocenteInvestigador] = []
        for objeto in self.__lista:
            if isinstance(objeto,DocenteInvestigador) and nomCarrera == objeto.getCarrera():
                lista.append(objeto)
        lista.sort(key=lambda x: x.getNombre())
        for elem in lista:
            print('Nombre: {}'.format(elem.getNombre()))

    def opcion5(self):
        area = input('Ingrese el area de investigacion:')
        contadorDI :int= 0
        contadorI:int = 0
        for objeto in self.__lista:
            if isinstance(objeto,DocenteInvestigador) and area == objeto.getArea():
                contadorDI += 1
            elif isinstance(objeto,Investigacion) and area == objeto.getArea():
                contadorI += 1
        print('Hay {} docentes investigadores y {} investigadores en la area {}'.format(contadorDI,contadorI,area))

    def opcion6(self):
        lista = list(self.__lista)        
        lista.sort(key=lambda x: x.getApellido())
        tipo = None
        sueldo:float = 0.0
        print('Nombre\t\tApellido\t\tTipo\t\t\tSueldo')
        for objeto in lista:
            valor = type(objeto)
            if valor == Docente:
                sueldo = objeto.sueldoDocente()
                tipo = "Docente"
            elif valor == Investigacion:
                sueldo = objeto.SueloaCobrar()
                tipo = "Investigador"
            elif valor == DocenteInvestigador:
                sueldo = objeto.SueldoDI()
                tipo = "DocenteInvestigador"
            elif valor == PersonalApoyo:
                sueldo = objeto.sueldoPersonalApoyo()
                tipo = "PersonalApoyo"
            #print('%2s%19s%30s%20.2f'%(objeto.getNombre(),objeto.getApellido(),tipo,sueldo))
            print('{:16}{:18}{:30}{:8}'.format(objeto.getNombre(),objeto.getApellido(),tipo,sueldo))

    def opcion7(self):
        categoria = input('Ingrese la categoria de investigacion:')
        lista: list[DocenteInvestigador] = []
        for objeto in self.__lista:
            if isinstance(objeto,DocenteInvestigador) and categoria == objeto.getCatetoria():
                lista.append(objeto)
        print('Apellido\t\tNombre\t\tImporte Extra')
        for elem in lista:
            print('%s%25s%20.2f'%(elem.getApellido(),elem.getNombre(),elem.getExtra()))

    def opcion8(self):
        self.__manejador.guardarJson(self.__lista)
    
    def opcion9(self):
        userPass = input('Ingrese el usuario y la contraseña: ')
        if userPass ==  "uTesoreso/ag@74ck":
            ManejadorTesorero(self.__lista)
        elif userPass == "uDirector/ufC77#!1":
            ManejadorDirector(self.__lista)

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
        elif opcion == 8:
            self.opcion8()
        elif opcion == 9:
            self.opcion9()
        else:
            print('Opcion no valida')