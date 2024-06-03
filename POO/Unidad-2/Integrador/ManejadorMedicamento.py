import csv
from ClaseMedicamento import Medicamento


class ManejadorMedicamento:
    __listaobjetos: list[Medicamento]
    def __init__(self):
        self.__listaobjetos = []

    def CargaM(self):
        with open("Integrador\medicamentos.csv", 'r',encoding='utf8') as archivo:
            reader = csv.reader(archivo,delimiter=(';'))
            next(reader,None)
            for linea in reader:
                print(linea)
                objeto = Medicamento(int(linea[0]),int(linea[1]),str(linea[2]),str(linea[3]),str(linea[4]),int(linea[5]),int(linea[6]))
                self.__listaobjetos.append(objeto)
    
    def mostrar(self,cama):
        i:int = 0
        print('\tMedicamento/Monodroga  \t\tPresentacion \t\tCantidad \tPrecio')
        for objeto in self.__listaobjetos:
            if cama == objeto.getIdcama():
                #print('%1s %1s %15s %15d %10d' %(objeto.getNombreM(),objeto.getMonodroga(),objeto.getPresentacion(),objeto.getCantidadAplicada(),objeto.getprecioTotal()))
                print('\t{}/{}\t\t{}      \t{}\t\t{}'.format(objeto.getNombreM(),objeto.getMonodroga(),objeto.getPresentacion(),objeto.getCantidadAplicada(),objeto.getprecioTotal()))