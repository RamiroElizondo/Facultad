from Email import Email

def test():
    objeto = Email('ramiro','gmail','com','123')
    print(objeto.retornaremail())
    con = objeto.comprobar('123')
    objeto.modificar('247')
    objeto2 = Email.crearcuenta('juanperez@gmail.com')

if __name__ == "__main__":
    test()
    nombre = input("Ingrese su Nombre: ")
    nombrec = input("Ingrese el nombre de la cuenta: ")
    idd = input('Ingresar ID de la cuenta: ')
    dom = input('Ingresar Dominio: ')
    tipo = input('Ingresar tipo de dominio: ')
    cont = input('Ingresa la contraseña: ')
    objeto1 = Email(idd, dom, tipo, cont)

    print('\nEstimado <{}>'.format(nombre))
    print('Te enviaremos tus mensajes a la direccion <{}>\n'.format(objeto1.retornaremail()))

    print("Modificar contraseña".center(30, '-'))
    contra1 = input("Ingrese la contraseña actual: ")
    con = objeto1.comprobar(contra1)

    if con is True:
        nueva1 = input('Ingrese la contraseña nueva: ')
        objeto1.modificar(nueva1)

    direccion = input('Ingrese la direccion de correo: ')
    objeto2 = Email.crearcuenta(direccion)
    print(objeto2.retornaremail())

    with open('Cuentas.txt', 'r', encoding='utf8') as archivo:
        lista = archivo.readline()
        listaN = lista.split(',')
        listaobjetos = list(map(lambda x: Email.crearcuenta(x), listaN))
        contador = 0
        idc = input("Ingrese un identificador de Cuenta: ")
        for cuenta in listaobjetos:
            if idc == cuenta.getidcuenta():
                contador = contador + 1
        if contador >= 1:
            print("Esta repetido")