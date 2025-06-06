import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import time



class TestCalculadoraIS3(unittest.TestCase):

    def setUp(self):
        # Configuración inicial del navegador
        self.driver = webdriver.Edge()
        self.driver.get("https://gerabarud.github.io/is3-calculadora/")
        self.driver.minimize_window()  # Espera a que la página cargue completamente 
        self.input_operador1 = self.driver.find_element(By.ID, "number1Field")
        self.input_operador2 = self.driver.find_element(By.ID, "number2Field")
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.selector_build= Select(self.driver.find_element(By.ID, "selectBuild"))
        self.selector_build.select_by_visible_text("Prototype")
        self.selector_operacion= Select(self.driver.find_element(By.ID, "selectOperationDropdown"))
        self.botonIntegers= self.driver.find_element(By.ID, "integerSelect")
        self.boton_calcular = self.driver.find_element(By.ID, "calculateButton")
        self.resultado = self.driver.find_element(By.ID, "numberAnswerField")

    def plantilla_test_resultado(self, operacion, operando1, operando2, resultado_esperado, entero=False):
        #Configurar operacion real o entera
        if entero:
            if not(self.botonIntegers.is_selected()):
                self.botonIntegers.click()

        # Configurar selectores
        self.selector_operacion.select_by_visible_text(operacion)

        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys(operando1)
        self.input_operador2.send_keys(operando2)
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

  
        # Verifica el resultado
        result = self.resultado.get_attribute("value")
        self.assertEqual(result, 
                         resultado_esperado, 
                         f"Error en la operación |{operacion}| con |{operando1}| y |{operando2}|. Se esperaba |{resultado_esperado}| pero se obtuvo |{result}|."
                         )

    def plantilla_test_error(self, operacion, operando1, operando2, resultado_esperado, entero=False):
        if entero:
            if not(self.botonIntegers.is_selected()):
                self.botonIntegers.click()

        # Configurar selectores
        self.selector_operacion.select_by_visible_text(operacion)

        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys(operando1)
        self.input_operador2.send_keys(operando2)
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Verifica el resultado
        error = self.driver.find_element(By.ID, "errorMsgField").text
        self.assertIsNotNone(error, "Error esperado no encontrado para la operación {operacion} con {operando1} y {operando2}. Se esperaba un mensaje de error pero no se encontró ninguno.")

    def test_caso_prueba1(self): # Prueba suma entera valida
        self.plantilla_test_resultado("Add", "9999999999", "9999999999", "19999999998", True)

    def test_caso_prueba2(self): # Prueba suma real valida
        self.plantilla_test_resultado("Add", "9.999999999", "9.999999999", "19.99999998")

    def test_caso_prueba3(self): # Prueba suma invalida op2
        self.plantilla_test_error("Add", "99999999999", "K", None)

    def test_caso_prueba4(self): # Prueba suma invalida op1
        self.plantilla_test_error("Add", "K", "99999999999", None)

    def test_caso_prueba5(self): # Prueba suma invalida ambos operadores
        self.plantilla_test_error("Add", "K", "A", None)

    def test_caso_prueba6(self): # Prueba resta entera valida
        self.plantilla_test_resultado("Subtract", "9999999999", "9999999999", "0", True)

    def test_caso_prueba7(self): # Prueba resta real valida
        self.plantilla_test_resultado("Subtract", "9999999999", "-999999999", "10999999998")

    def test_caso_prueba8(self): # Prueba resta invalida op2
        self.plantilla_test_error("Subtract", "99999999999", "M", None)

    def test_caso_prueba9(self): # Prueba resta invalida op1
        self.plantilla_test_error("Subtract", "E", "99999999999", None)

    def test_caso_prueba10(self): # Prueba suma invalida ambos operadores
        self.plantilla_test_error("Subtract", "E", "M", None)

    def test_caso_prueba11(self): # Prueba multiplicacion entera valida
        self.plantilla_test_resultado("Multiply", "9999999999", "9999999999", "99999999980000000001", True)

    def test_caso_prueba12(self): # Prueba multiplicacion real valida
        self.plantilla_test_resultado("Multiply", "-9.9999999", "9.999999999", "-99.999998900000001")

    def test_caso_prueba13(self): # Prueba multiplicacion invalida op1
        self.plantilla_test_error("Multiply", "e8.", "9999999999", None)
        
    def test_caso_prueba14(self): # Prueba multiplicacion invalida op2
        self.plantilla_test_error("Multiply", "99999999999", "-.", None)

    def test_caso_prueba15(self): # Prueba division entera valida
        self.plantilla_test_resultado("Divide", "9999999999", "9999999999", "1", True)

    def test_caso_prueba16(self): # Prueba division real valida
        self.plantilla_test_resultado("Divide", "9999999999", "999.99999", "10000000.099000001")

    def test_caso_prueba17(self): # Prueba division entera valida primer operando menor
        self.plantilla_test_resultado("Divide", "99999", "9999999999", "0", True)

    def test_caso_prueba18(self): # Prueba division entera invalida
        if not(self.botonIntegers.is_selected()):
            self.botonIntegers.click()
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Divide")
        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("9999999999")
        self.input_operador2.send_keys("0")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        result = self.resultado.get_attribute("value")
        error = self.driver.find_element(By.ID, "errorMsgField").text
        self.assertTrue(result == "Infinity" or result == "-Infinity" or error!=None, "CP 18 fallo.")

    def test_caso_prueba19(self): # Prueba division entera invalida       
        if not(self.botonIntegers.is_selected()):
            self.botonIntegers.click()
        # Configurar selectores
        self.selector_operacion.select_by_visible_text("Divide")
        # Encuentra el campo de entrada y envía una expresión matemática
        self.input_operador1.clear()
        self.input_operador2.clear()
        self.input_operador1.send_keys("0")
        self.input_operador2.send_keys("0")
        
        # Encuentra el botón de suma y haz clic en él
        self.boton_calcular.click()

        # Espera un momento para que se procese la solicitud
        time.sleep(2)

        # Verifica el resultado
        result = self.resultado.get_attribute("value")
        error = self.driver.find_element(By.ID, "errorMsgField").text
        self.assertTrue(result == "Infinity" or result == "-Infinity" or error!=None, "CP 19 fallo.")

    def test_caso_prueba20(self): # Prueba concatenacion valida
        self.plantilla_test_resultado("Concatenate", "ABCDEFGHIJ", "KMNLOPQRST", "ABCDEFGHIJKMNLOPQRST")

    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
