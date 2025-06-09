import unittest
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

class TestCalculadoraTelefono(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.platform_version = "12"
        options.device_name = "a31"
        options.automation_name = "UiAutomator2"
        options.app_package = "com.sec.android.app.popupcalculator"
        options.app_activity = ".Calculator t526"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

        cls.button_ids = {
            '0': 'calc_keypad_btn_00',
            '1': 'calc_keypad_btn_01',
            '2': 'calc_keypad_btn_02',
            '3': 'calc_keypad_btn_03',
            '4': 'calc_keypad_btn_04',
            '5': 'calc_keypad_btn_05',
            '6': 'calc_keypad_btn_06',
            '7': 'calc_keypad_btn_07',
            '8': 'calc_keypad_btn_08',
            '9': 'calc_keypad_btn_09',
            '+': 'calc_keypad_btn_add',
            '-': 'calc_keypad_btn_sub',
            '*': 'calc_keypad_btn_mul',
            '/': 'calc_keypad_btn_div',
            '.': 'calc_keypad_btn_dot',
            '=': 'calc_keypad_btn_equal',
            'DEL': 'calc_keypad_btn_clear',
        }

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def press_button(self, char):
        if char in self.button_ids:
            try:
                self.driver.find_element(AppiumBy.ID, f"com.sec.android.app.popupcalculator:id/{self.button_ids[char]}").click()
            except:
                pass  # ignorar si no existe, para caracteres inválidos

    def clear_input(self):
        self.driver.find_element(AppiumBy.ID, f"com.sec.android.app.popupcalculator:id/{self.button_ids['DEL']}").click()

    def enter_expression(self, expr):
        for char in expr:
            if char.strip():
                self.press_button(char)

    def calcular(self, op1, operador, op2):
        self.clear_input()
        self.enter_expression(op1)
        self.press_button(operador)
        self.enter_expression(op2)
        self.press_button('=')
        time.sleep(1)
        result = self.driver.find_element(AppiumBy.ID, "com.sec.android.app.popupcalculator:id/calc_edt_formula").text
        return result.replace(',', '')

    def plantilla_test_resultado(self, operador, op1, op2, esperado):
        resultado = self.calcular(op1, operador, op2)
        self.assertEqual(resultado, esperado,
                         f"{op1} {operador} {op2} = {resultado}\nEsperado: {esperado}")

    def plantilla_test_error(self, operador, op1, op2):
        resultado = self.calcular(op1, operador, op2)
        self.assertTrue(resultado in ["", "Infinity", "-Infinity", "∞", "Error", "Can't divide by 0", "0"],
                        f"Se esperaba error, pero se obtuvo: {resultado}")

    # Casos válidos
    def test_cp1(self): self.plantilla_test_resultado('+', '9999999999', '9999999999', '19999999998')
    def test_cp2(self): self.plantilla_test_resultado('+', '9.999999999', '9.999999999', '19.99999998')
    def test_cp6(self): self.plantilla_test_resultado('-', '9999999999', '9999999999', '0')
    def test_cp7(self): self.plantilla_test_resultado('-', '9999999999', '-999999999', '10999999998')
    def test_cp11(self): self.plantilla_test_resultado('*', '9999999999', '9999999999', '99999999980000000001')
    def test_cp12(self): self.plantilla_test_resultado('*', '-9.9999999', '9.999999999', '-99.999998900000001')
    def test_cp15(self): self.plantilla_test_resultado('/', '9999999999', '9999999999', '1')
    def test_cp16(self): self.plantilla_test_resultado('/', '9999999999', '999.99999', '10000000.099000001')
    def test_cp17(self): self.plantilla_test_resultado('/', '99999', '9999999999', '0')

    # Casos inválidos
    def test_cp3(self): self.plantilla_test_error('+', '99999999999', 'K')
    def test_cp4(self): self.plantilla_test_error('+', 'K', '99999999999')
    def test_cp5(self): self.plantilla_test_error('+', 'K', 'A')
    def test_cp8(self): self.plantilla_test_error('-', '99999999999', 'M')
    def test_cp9(self): self.plantilla_test_error('-', 'E', '99999999999')
    def test_cp10(self): self.plantilla_test_error('-', 'E', 'M')
    def test_cp13(self): self.plantilla_test_error('*', 'e8.', '9999999999')
    def test_cp14(self): self.plantilla_test_error('*', '99999999999', '-.')
    def test_cp18(self): self.plantilla_test_error('/', '9999999999', '0')
    def test_cp19(self): self.plantilla_test_error('/', '0', '0')

    def test_cp20(self):
        print("\nCP20 omitido: concatenación de cadenas no es compatible con la calculadora Android.")

if __name__ == "__main__":
    unittest.main()
