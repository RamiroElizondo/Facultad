from Pago import Pago

class Cheque(Pago):
    __numeroCheque: int = 0

    def __init__(self,fecha,monto,numeroCheque):
        super().__init__(fecha,monto)
        self.__numeroCheque = numeroCheque
    
    def mostrar_detalles(self):
        print('Cheque\n')
        print('Fecha -{}- Monto {}- Numero de cheque: -{}-'.format(self.getFecha(),self.getMonto(),self.__numeroCheque))

if __name__ == '__main__':
    objeto = Cheque('20/01',2000,3)
    objeto.mostrar_detalles()