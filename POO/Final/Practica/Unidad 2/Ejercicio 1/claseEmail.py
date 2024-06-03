class Email:
    __idCuenta = ""
    __dominio = ""
    __tipo_dominio = ""
    __contra = ""

    def __init__(self,idcuenta,dominio,tipo,contra=None):
        self.__idCuenta = idcuenta
        self.__dominio = dominio
        self.__tipo_dominio = tipo
        self.__contra = contra

    def retornarEmail(self):
        return self.__idCuenta + '@' + self.__dominio + '.' + self.__tipo_dominio

    def getDominio(self):
        return self.__dominio
    
    def getContra(self):
        return self.__contra
    
    def setContra(self,nueva):
        self.__contra = nueva

    @staticmethod
    def crearCuenta(direccion):
        componentes = direccion.split(sep='@')
        dominiotipo = componentes[1].split(sep='.')
        return Email(componentes[0], dominiotipo[0], dominiotipo[1])

    def Mostrar(self):
        return Email.retornarEmail(self)
    
    def getIdentificador(self):
        return self.__idCuenta
