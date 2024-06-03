from Pago import Pago

class Transferencia(Pago):
    __cuentaDestino:str = ""
    __cuentaOrigen:str = ""

    def __init__(self,fecha,monto,cuentaDestino,cuentaOrigen):
        super().__init__(fecha,monto)
        self.__cuentaDestino = cuentaDestino
        self.__cuentaOrigen = cuentaOrigen
    
    def mostrar_detalles(self):
        print('Tranferencia\n')
        print('Fecha: -{}- Monto: -{}- Cuenta Origen: {} Cuenta Destino: -{}'.format(self.getFecha(),self.getMonto(),self.__cuentaOrigen,self.__cuentaDestino))
