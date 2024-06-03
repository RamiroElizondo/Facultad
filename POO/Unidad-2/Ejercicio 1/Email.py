class Email:
    __idcuenta = ""
    __dominio = ""
    __tipod = ""
    __contra = ""

    def __init__(self, idcuenta, dominio, tipod, contra=None):
        self.__idcuenta = idcuenta
        self.__dominio = dominio
        self.__tipod = tipod
        self.__contra = contra

    def retornaremail(self):
        return self.__idcuenta + '@' + self.__dominio + '.' + self.__tipod

    def getidcuenta(self):
        return self.__idcuenta

    def getdominio(self):
        return self.__dominio

    """def mostrar(self):
        print(f'Dominio: {self.__dominio}')
    """
    def getcontra(self):
        return self.__contra

    def comprobar(self, contra):
        if contra == self.__contra:
            condicion = True
            return condicion
        else:
            print("La contraseña no son iguales")

    def modificar(self, nueva):
        self.__contra = nueva
        print("Se modifico con exito".center(30, '-'))

    @staticmethod
    def crearcuenta(direc):
        var = direc.split("@")
        var1 = var[1].split(".")
        return Email(var[0], var1[0], var1[1])
