from decimal import Decimal, InvalidOperation
import re

resultado = '1.00000000E Más 20 Resultado del cálculo'
# Arregla notación científica localizada (idioma español)
resultado = resultado.replace("E Más ", "E+").replace("E más ", "E+")
resultado = resultado.replace("E Menos ", "E-").replace("E menos ", "E-")
print(f"Resultado original: {resultado}")
# Buscar número en notación científica o decimal
match = re.search(r'-?\d+(\.\d+)?(e[+-]?\d+)?', resultado, re.IGNORECASE)
numero = match.group() if match else ""
esperado = 9999999999
resultado_normalizado = Decimal(numero)
esperado_normalizado = Decimal(esperado)



print(f"Resultado: {resultado_normalizado}, Esperado: {esperado_normalizado}")



print("Cp1:",9999999999 + 9999999999)
print("Cp2:",9.999999999 + 9.999999999)
print("Cp6:",9999999999 - 9999999999)
print("Cp7:",9999999999 - -999999999)
print("Cp11:",9999999999 * 9999999999)
print("Cp12:",-9.9999999 * 9.999999999)
print("Cp15:",9999999999 / 9999999999)
print("Cp16:",9999999999 / 999.99999)
print("Cp17:",99999 / 9999999999)
print("Cp3:", "Error")
print("Cp4:", "Error")
