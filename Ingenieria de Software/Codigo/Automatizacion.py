from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Automatizacion:
    def __init__(self, device_name="a31", platform_version="12"):
        self.options = UiAutomator2Options()
        self.options.platform_name = "Android"
        self.options.platform_version = platform_version
        self.options.device_name = device_name
        self.options.automation_name = "UiAutomator2"
        self.options.app_package = "com.android.chrome"
        self.options.app_activity = "com.google.android.apps.chrome.Main t604"
        self.options.auto_grant_permissions = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=self.options)
        print("Contextos disponibles:", self.driver.contexts)

        self.driver.switch_to.context('WEBVIEW_chrome')
    
    def iniciar_app(self):
        time.sleep(5)
        for xpath in [
            "//*[@text='Usar sin una cuenta']",
            "//*[@text='Sí, acepto']",
            "//*[@text='Más']",
            "//*[@text='Entendido']"
        ]:
            try:
                self.driver.find_element(AppiumBy.XPATH, xpath).click()
                time.sleep(2)
            except:
                pass
    
    def navegar_a_web(self, url="https://automationexercise.com/"):
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 20)
        try:
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text, 'Automation')]")))
            print("Página cargada correctamente.")
        except:
            print("No se pudo verificar la carga de la página.")
    
    def cerrar_app(self):
        self.driver.quit()
    
    def ejecutar(self):
        self.iniciar_app()
        self.navegar_a_web()
        

    def ingresar_SeccionTest(self, xpath):
        print("//*[@text="+xpath+"]")
        try:
            self.driver.find_element(AppiumBy.XPATH,"//*[@text="+xpath+"]").click()
            time.sleep(2)
            print(f"Ingresando a la sección: {xpath}")
        except Exception as e:
            print(f"Error al ingresar a la sección {xpath}: {e}")
        time.sleep(60)
    def agregar_producto_por_nombre(self, nombre_buscado):
        # Buscamos todos los productos en pantalla
        productos = self.driver.find_elements(By.CLASS_NAME, "product-image-wrapper")
        print(productos)
        for idx, producto in enumerate(productos):
            try:
                print('Dentro del for y try')
                nombre_elemento = producto.find_element(AppiumBy.TAG_NAME, "p")
                nombre = nombre_elemento.text.strip()
                print(f"[{idx}] Producto encontrado: {nombre}")
                print(f"Comparando con: {nombre_buscado}")
                if nombre.lower() == nombre_buscado.lower():
                    print('Es igual')
                    print(f"Producto '{nombre}' encontrado. Agregando al carrito...")
                    boton = producto.find_element(AppiumBy.CLASS_NAME, "add-to-cart")
                    boton.click()
                    return True
            except Exception as e:
                print(f"[{idx}] No se pudo procesar un producto: {e}")
        print(f"No se encontró el producto con nombre: {nombre_buscado}")
        return False

if __name__ == "__main__":
    automatizacion = Automatizacion()
    automatizacion.ejecutar()
    automatizacion.agregar_producto_por_nombre("Blue Top")
    time.sleep(60)
    #automatizacion.ingresar_SeccionTest("Test Cases")
    automatizacion.cerrar_app()