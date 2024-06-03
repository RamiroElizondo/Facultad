from numpy import False_
from ManejadorIntegrantes import ManejadorIntegrante
from ManejadorProyecto import ManejadorProyecto


if __name__ == '__main__':
    manejadorI = ManejadorIntegrante()
    manejadorP = ManejadorProyecto()
    manejadorI.cargarArregloI()
    manejadorP.cargarListaP()
    lista = manejadorP.obtener()
    puntajes: list[int] = []
    for proyecto in lista:
        p1:int=manejadorI.calcular1(proyecto)
        p2:int=manejadorI.calcular2(proyecto)
        p3:int=manejadorI.calcular3(proyecto)
        valor1=manejadorI.calcular4(proyecto)
        valor2=manejadorI.calcular5(proyecto)
        if valor1 == False:
            print('<<El Proyecto {} debe tener un Directo>>'.format(proyecto))
            
        if valor2 == False: 
            print('<<El Proyecto {} debe tener un Codirector>>'.format(proyecto))
        
        p4:int=0
        if valor1 == False or valor2 == False:
            p4:int=-10
        
        totalP = p1+p2+p3+p4
        puntajes.append(totalP)
    manejadorP.cargarPuntaje(puntajes)
    manejadorP.listarMayorMenor()