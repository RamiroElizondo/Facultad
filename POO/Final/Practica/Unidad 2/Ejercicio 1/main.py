import csv
from claseEmail import Email


if '__main__' == __name__:

    print('Inicio Secion'.center(40,'-'))
    nombre = input('Ingrese su nombre: ')
    idcuenta = input('Ingrese el identificador de cuenta: ')
    dominio = input('Ingrese el dominio: ')
    tipo_dominio = input('Ingrese el tipo de dominio: ')
    contra = input('Ingrese la constraseña: ')
    persona1 = Email(idcuenta, dominio, tipo_dominio, contra)

    direccionP1 = persona1.retornarEmail()
    print('Estimado <{}> te enviaremos tus mensajes a la direccion <{}>'.format(nombre,direccionP1))

    print('Modificar Contraseña'.center(40,'-'))
    contraVieja = input('Ingrese la contraseña vieja: ')
    
    while contraVieja != persona1.getContra():
        print('La contraseña no es igual')
        contraVieja = input('Ingrese la contraseña vieja: ')

    contraNueva = input('Ingrese la contraseña nueva: ')
    persona1.setContra(contranueva)

    correo = input('Ingrese un direccion de correo: ')
    persona2 = Email.crearCuenta(correo)
    print(persona2.retornarEmail())

    with open("Unidad 2\Ejercicio 1\cuentas.csv",'r',encoding='utf8') as archivo:
        listaCorreos = archivo.readline() 
        listaCorreos = listaCorreos.split(sep=',')
        listaobjetos = []
        
        for correo in listaCorreos:
            objeto = Email.crearCuenta(correo)
            listaobjetos.append(objeto)
        
        
        identificador = input('Ingrese identificador de cuenta: ')
        repeticiones = 0
        for objeto in listaobjetos:
            if objeto.getIdentificador() == identificador:
                repeticiones += 1
        
        print('Esta repetido {} veces'.format(repeticiones))