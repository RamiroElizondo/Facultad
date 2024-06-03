"""
try:
    # Se realizan varias operaciones
    a = 10
    b = 2
    c = a + b
    d = a - b
    e = a * b
    f = a / 0 # Se produce una excepción ZeroDivisionError
except ZeroDivisionError:
    print("No se puede dividir entre cero")
else:
    # Se ejecuta si no se produce ninguna excepción
    print("Resultado de la suma: ", c)
    print("Resultado de la resta: ", d)
    print("Resultado de la multiplicación: ", e)
    print("Resultado de la división: ", f)
finally:
    # Se ejecuta siempre al final, haya o no excepciones
    print("Operaciones finalizadas")



def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b


try:
    # Se realizan varias invocaciones a funciones
    a = 10
    b = 2
    c = sumar(a, b)
    d = restar(a, b)
    e = multiplicar(a, b)
    f = dividir(a, 0) # Se produce una excepción ZeroDivisionError

    print('Llegue aca')
except ZeroDivisionError as ex:
    print(ex)
else:
    # Se ejecuta si no se produce ninguna excepción
    print("Resultado de la suma: ", c)
    print("Resultado de la resta: ", d)
    print("Resultado de la multiplicación: ", e)
    print("Resultado de la división: ", f)
finally:
    # Se ejecuta siempre al final, haya o no excepciones
    print("Operaciones finalizadas")
"""

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b

try:
    # Se realizan varias invocaciones a funciones
    a = 10
    b = 2
    print("Resultado de la suma: ", sumar(a, 'b'))
    print("Resultado de la resta: ", restar(a, b))
    print("Resultado de la multiplicación: ", multiplicar(a, b))
    print("Resultado de la división: ", dividir(a, 0)) # Se produce una excepción ZeroDivisionError
    print('Posible Operaciones Siguientes')
except ZeroDivisionError as ex:
    print(ex)
except TypeError as ex:
    print(ex)
except Exception as ex:
    print('Entre el Tercer except',ex)
finally:
    # Se ejecuta siempre al final, haya o no excepciones
    print("Operaciones finalizadas")

print('continuamos')