import csv
from PlanAhorro import PlanAhorro


class ManejadorPlan:
    __listaobjetos: list[PlanAhorro]

    def __init__(self):
        self.__listaobjetos = []

    def test(self):
        objeto = PlanAhorro(1,'hilux','4x4',2000000)
        objeto.setcantCuotasP(15)
        objeto.setcantCuotasLicitar(80)
        objeto.setvalorVehiculo(3000000)
        objeto.muestra()
        objeto.mostrar()

    def cargarObjetos(self):
        with open('Unidad-2-POO\Ejercicio 5\planes.csv', 'r', encoding='utf8') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            for linea in reader:
                objeto = PlanAhorro(int(linea[0]),str(linea[1]),str(linea[2]),int(linea[3]))
                PlanAhorro.setcantCuotasP(int(linea[4]))
                PlanAhorro.setcantCuotasLicitar(int(linea[5]))
                self.__listaobjetos.append(objeto)
            
            """for i in self.__listaobjetos:
                print(i,end=' ')
                i.mostrar()"""
        #return self.__listaobjetos

    def modificar(self):
        for obj in self.__listaobjetos:
            obj.muestra()
            valorNuevo= int(input('Ingrese el nuevo valor del vehiculo: '))
            obj.setvalorVehiculo(valorNuevo)

    def mostrarDatos(self):
        valor = int(input('Ingrese valor: '))
        for objetoo in self.__listaobjetos:
            valorcuota:float = (objetoo.getvalorVehiculo() / objetoo.getcantCuotasP())+objetoo.getvalorVehiculo()*0.10
            #print(valorcuota)
            if valorcuota < valor:
                objetoo.muestra()
    
    def mostrarMonto(self):
        for ob in self.__listaobjetos:
            print('Plan %d' %ob.getcod())
            valorcuota:float = (ob.getvalorVehiculo() / ob.getcantCuotasP())+ob.getvalorVehiculo()*0.10
            monto:float=valorcuota*ob.getcantCuotasLicitar()
            print('Monto que debe haber pagado para licitar: %.2f'%monto)
    
    def modificarCantidadCuotas(self):
        cantidad = int(input('Ingrese la nueva cantidad de cuotas: '))
        PlanAhorro.setcantCuotasLicitar(cantidad)
        print('Se modifico'.center(30,'-'))
        print()