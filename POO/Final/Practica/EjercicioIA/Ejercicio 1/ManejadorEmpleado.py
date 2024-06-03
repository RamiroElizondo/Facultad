from Pago import Pago
from Tranferencia import Transferencia
from Cheque import Cheque
from Empleado import Empleado

class ManejadorEmpleado:
    __listaEmpleados: list[Empleado]
    
    def __init__(self):
        self.__listaEmpleados = []

    def agregarEmpleados(self):
        cant = int(input('Cuales es la cantidad de empleado: '))
        for i in range(0,cant):
            print('Empleado {}\n'.format(i))
            nombre = input('Ingrese nombre: ')
            apellido = input('Ingrese apellido: ')
            sueldo = input('Ingrese sueldo: ')
            objeto = Empleado(nombre,apellido,sueldo)
            self.__listaEmpleados.append(objeto)
           
    def pagar(self):
        for empleado in self.__listaEmpleados:
            print('Empleado: {}'.format(empleado.getNombre()))
            fecha = input('Ingrese fecha de pago: ')
            monto = int(input('Ingrese el monto: '))
            metodo = input('Cheque o Transferencia')
            if metodo == 'Cheque':
                numero = int(input('Ingrese numero de cheque: '))
                empleado.pagoSueldo(Cheque(fecha,monto,numero))
            elif metodo == 'Transferencia':
                origen = input('Ingrese la cuenta de Origen: ')
                destino = input('Ingrese la cuenta de Destino')
                empleado.pagoSueldo(Transferencia(fecha,monto,destino,origen))
    
    def mostrar(self):
        for empleado in self.__listaEmpleados:
            print('Nombre: {} Apellido: {}'.format(empleado.getNombre(),empleado.getApellido()))
            for pago in empleado.getLista():
                print(pago.mostrar_detalles())


"""
Juan
Perez
5000
María
Rodriguez
6000
Pedro
Gonzalez
4000
"""