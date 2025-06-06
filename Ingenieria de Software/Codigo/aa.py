from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Automatizacion:
    def __init__(self, device_name="a31", platform_version="12", appium_server="http://localhost:4723/wd/hub"):
        """
        Inicializar la automatización con configuración mejorada
        """
        self.setup_logging()
        
        # Configuración de opciones para UiAutomator2
        self.options = UiAutomator2Options()
        self.options.platform_name = "Android"
        self.options.platform_version = platform_version
        self.options.device_name = device_name
        self.options.automation_name = "UiAutomator2"
        self.options.app_package = "com.android.chrome"
        self.options.app_activity = "com.google.android.apps.chrome.Main"
        self.options.auto_grant_permissions = True
        self.options.no_reset = True
        self.options.new_command_timeout = 300
        
        try:
            self.driver = webdriver.Remote(appium_server, options=self.options)
            self.wait = WebDriverWait(self.driver, 20)
            self.logger.info("Driver iniciado correctamente")
            
            # Mostrar contextos disponibles
            contextos = self.driver.contexts
            self.logger.info(f"Contextos disponibles: {contextos}")
            
            print(contextos)
            # Cambiar a contexto web si está disponible
            if 'WEBVIEW_chrome' in contextos:
                self.driver.switch_to.context('WEBVIEW_chrome')
                self.logger.info("Cambiado a contexto WEBVIEW_chrome")
            else:
                self.logger.warning("Contexto WEBVIEW_chrome no disponible")
                
        except Exception as e:
            self.logger.error(f"Error al inicializar driver: {e}")
            raise

    def setup_logging(self):
        """
        Configurar sistema de logging
        """
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('automation.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def iniciar_app(self):
        """
        Manejar diálogos iniciales de Chrome con mejor lógica
        """
        self.logger.info("Iniciando aplicación y manejando diálogos...")
        time.sleep(3)
        
        dialogos_chrome = [
            "//*[@text='Usar sin una cuenta']",
            "//*[@text='No, gracias']", 
            "//*[@text='Sí, acepto']",
            "//*[@text='Aceptar']",
            "//*[@text='Más']",
            "//*[@text='Entendido']",
            "//*[@text='Permitir']",
            "//*[@text='Continuar']"
        ]
        
        for xpath in dialogos_chrome:
            try:
                elemento = self.driver.find_element(AppiumBy.XPATH, xpath)
                if elemento.is_displayed():
                    elemento.click()
                    self.logger.info(f"Diálogo cerrado: {xpath}")
                    time.sleep(2)
            except NoSuchElementException:
                continue
            except Exception as e:
                self.logger.warning(f"Error al cerrar diálogo {xpath}: {e}")

    def navegar_a_web(self, url="https://automationexercise.com/"):
        """
        Navegar a la página web con mejor verificación
        """
        try:
            self.logger.info(f"Navegando a: {url}")
            self.driver.get(url)
            
            # Esperar a que la página cargue completamente
            self.wait.until(
                EC.any_of(
                    EC.presence_of_element_located((AppiumBy.XPATH, "//*[text(), 'Automation']")),
                    EC.presence_of_element_located((AppiumBy.XPATH, "//*[text(), 'Exercise']")),
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
            )
            
            # Verificar título de la página
            titulo = self.driver.title
            self.logger.info(f"Página cargada. Título: {titulo}")
            
            # Tomar screenshot de confirmación
            self.tomar_screenshot("pagina_cargada.png")
            return True
            
        except TimeoutException:
            self.logger.error("Timeout: La página no cargó en el tiempo esperado")
            return False
        except Exception as e:
            self.logger.error(f"Error al navegar: {e}")
            return False

    def ingresar_seccion_test(self, nombre_seccion):
        """
        Ingresar a una sección específica con mejor manejo
        """
        xpath_opciones = [
            f"//*[@text='{nombre_seccion}']",
            f"//a[contains(text(), '{nombre_seccion}')]",
            f"//*[contains(@text, '{nombre_seccion}')]"
        ]
        
        self.logger.info(f"Intentando ingresar a la sección: {nombre_seccion}")
        
        for xpath in xpath_opciones:
            try:
                elemento = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath)))
                elemento.click()
                self.logger.info(f"Ingresado a la sección: {nombre_seccion}")
                time.sleep(3)
                self.tomar_screenshot(f"seccion_{nombre_seccion.replace(' ', '_').lower()}.png")
                return True
            except TimeoutException:
                continue
            except Exception as e:
                self.logger.warning(f"Error con xpath {xpath}: {e}")
                continue
        
        self.logger.error(f"No se pudo ingresar a la sección: {nombre_seccion}")
        return False

    def scroll_hasta_encontrar_elemento(self, locator_type, locator_value, max_scrolls=5):
        """
        Hacer scroll hasta encontrar un elemento específico
        """
        for i in range(max_scrolls):
            try:
                if locator_type == "xpath":
                    elemento = self.driver.find_element(AppiumBy.XPATH, locator_value)
                elif locator_type == "class":
                    elemento = self.driver.find_element(AppiumBy.CLASS_NAME, locator_value)
                else:
                    return None
                
                if elemento.is_displayed():
                    return elemento
            except NoSuchElementException:
                pass
            
            # Hacer scroll hacia abajo
            self.driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
        
        return None

    def agregar_producto_por_nombre(self, nombre_buscado):
        """
        Buscar y agregar producto al carrito con mejor lógica
        """
        self.logger.info(f"Buscando producto: {nombre_buscado}")
        
        try:
            # Navegar a la sección de productos si no estamos ahí
            if not self.ingresar_seccion_test("Products"):
                self.logger.warning("No se pudo acceder a la sección Products")
            
            time.sleep(3)
            
            # Buscar productos con scroll si es necesario
            max_intentos = 3
            for intento in range(max_intentos):
                productos = self.driver.find_elements(By.CLASS_NAME, "product-image-wrapper")
                self.logger.info(f"Intento {intento + 1}: Encontrados {len(productos)} productos")
                
                if not productos:
                    self.driver.execute_script("window.scrollBy(0, 800);")
                    time.sleep(2)
                    continue
                
                for idx, producto in enumerate(productos):
                    try:
                        # Buscar el nombre del producto
                        nombre_elemento = producto.find_element(AppiumBy.TAG_NAME, "p")
                        nombre = nombre_elemento.text.strip()
                        self.logger.info(f"[{idx}] Producto encontrado: '{nombre}'")
                        
                        if nombre.lower() == nombre_buscado.lower():
                            self.logger.info(f"¡Producto '{nombre}' encontrado! Agregando al carrito...")
                            
                            # Buscar el botón de agregar al carrito
                            try:
                                boton = producto.find_element(AppiumBy.CLASS_NAME, "add-to-cart")
                                # Hacer scroll hasta el botón si es necesario
                                self.driver.execute_script("arguments[0].scrollIntoView(true);", boton)
                                time.sleep(1)
                                boton.click()
                                
                                self.logger.info("Producto agregado al carrito exitosamente")
                                self.tomar_screenshot("producto_agregado.png")
                                
                                # Manejar modal de confirmación si aparece
                                self.manejar_modal_confirmacion()
                                return True
                                
                            except NoSuchElementException:
                                # Intentar con otros selectores para el botón
                                selectores_boton = [
                                    ".//a[contains(@class, 'add-to-cart')]",
                                    ".//button[contains(text(), 'Add to cart')]",
                                    ".//a[contains(text(), 'Add to cart')]"
                                ]
                                
                                for selector in selectores_boton:
                                    try:
                                        boton = producto.find_element(AppiumBy.XPATH, selector)
                                        boton.click()
                                        self.logger.info("Producto agregado con selector alternativo")
                                        return True
                                    except:
                                        continue
                                
                                self.logger.error("No se encontró el botón 'Add to cart'")
                    
                    except Exception as e:
                        self.logger.warning(f"[{idx}] Error al procesar producto: {e}")
                        continue
                
                # Si no encontramos el producto, hacer scroll y continuar
                if intento < max_intentos - 1:
                    self.driver.execute_script("window.scrollBy(0, 800);")
                    time.sleep(2)
            
            self.logger.error(f"No se encontró el producto: {nombre_buscado}")
            return False
            
        except Exception as e:
            self.logger.error(f"Error general al buscar producto: {e}")
            return False

    def manejar_modal_confirmacion(self):
        """
        Manejar modal de confirmación después de agregar producto
        """
        try:
            # Esperar por el modal de confirmación
            modal_xpaths = [
                "//*[contains(text(), 'Added')]",
                "//*[contains(text(), 'Continue Shopping')]",
                "//*[contains(text(), 'View Cart')]"
            ]
            
            for xpath in modal_xpaths:
                try:
                    elemento = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((AppiumBy.XPATH, xpath))
                    )
                    self.logger.info("Modal de confirmación detectado")
                    
                    # Hacer clic en "Continue Shopping" si está disponible
                    try:
                        continuar = self.driver.find_element(AppiumBy.XPATH, "//*[contains(text(), 'Continue Shopping')]")
                        continuar.click()
                        self.logger.info("Continuando con las compras")
                    except:
                        pass
                    
                    break
                except TimeoutException:
                    continue
                    
        except Exception as e:
            self.logger.info(f"No se detectó modal de confirmación: {e}")

    def tomar_screenshot(self, nombre_archivo):
        """
        Tomar captura de pantalla
        """
        try:
            self.driver.save_screenshot(nombre_archivo)
            self.logger.info(f"Screenshot guardado: {nombre_archivo}")
        except Exception as e:
            self.logger.error(f"Error al tomar screenshot: {e}")

    def obtener_info_pagina(self):
        """
        Obtener información básica de la página actual
        """
        try:
            titulo = self.driver.title
            url = self.driver.current_url
            self.logger.info(f"Título: {titulo}")
            self.logger.info(f"URL: {url}")
            return {"titulo": titulo, "url": url}
        except Exception as e:
            self.logger.error(f"Error al obtener info de página: {e}")
            return None

    def buscar_producto_en_buscador(self, termino_busqueda):
        """
        Usar el buscador de la página para encontrar productos
        """
        try:
            # Buscar el campo de búsqueda
            search_selectors = [
                "//input[@placeholder='Search Product']",
                "//input[@name='search']",
                "//input[@id='search_product']"
            ]
            
            campo_busqueda = None
            for selector in search_selectors:
                try:
                    campo_busqueda = self.driver.find_element(AppiumBy.XPATH, selector)
                    break
                except:
                    continue
            
            if not campo_busqueda:
                self.logger.error("No se encontró el campo de búsqueda")
                return False
            
            # Escribir término de búsqueda
            campo_busqueda.clear()
            campo_busqueda.send_keys(termino_busqueda)
            
            # Buscar botón de búsqueda
            boton_buscar = self.driver.find_element(AppiumBy.XPATH, "//button[@id='submit_search']")
            boton_buscar.click()
            
            self.logger.info(f"Búsqueda realizada: {termino_busqueda}")
            time.sleep(3)
            return True
            
        except Exception as e:
            self.logger.error(f"Error al buscar producto: {e}")
            return False

    def cerrar_app(self):
        """
        Cerrar la aplicación con manejo de errores
        """
        try:
            if hasattr(self, 'driver') and self.driver:
                self.driver.quit()
                self.logger.info("Aplicación cerrada correctamente")
        except Exception as e:
            self.logger.error(f"Error al cerrar aplicación: {e}")

    def ejecutar_prueba_completa(self):
        """
        Ejecutar una prueba completa de automatización
        """
        try:
            self.logger.info("=== INICIANDO PRUEBA COMPLETA ===")
            
            # Paso 1: Iniciar app y manejar diálogos
            self.iniciar_app()
            
            # Paso 2: Navegar a la web
            if not self.navegar_a_web():
                return False
            
            # Paso 3: Obtener información de la página
            self.obtener_info_pagina()
            
            # Paso 4: Agregar producto específico
            producto_objetivo = "Blue Top"
            if self.agregar_producto_por_nombre(producto_objetivo):
                self.logger.info(f"✅ Producto '{producto_objetivo}' agregado exitosamente")
            else:
                self.logger.error(f"❌ No se pudo agregar el producto '{producto_objetivo}'")
            
            # Paso 5: Ingresar a Test Cases (opcional)
            # self.ingresar_seccion_test("Test Cases")
            
            self.logger.info("=== PRUEBA COMPLETA FINALIZADA ===")
            return True
            
        except Exception as e:
            self.logger.error(f"Error durante la prueba completa: {e}")
            return False


def main():
    """
    Función principal mejorada
    """
    automatizacion = None
    try:
        # Crear instancia con configuración personalizada
        automatizacion = Automatizacion(
            device_name="a31",  # Cambia por tu dispositivo
            platform_version="12"  # Cambia por tu versión de Android
        )
        
        # Ejecutar prueba completa
        automatizacion.ejecutar_prueba_completa()
        
        # Mantener la aplicación abierta por un tiempo para observar
        time.sleep(10)
        
    except KeyboardInterrupt:
        print("\n❌ Prueba interrumpida por el usuario")
    except Exception as e:
        print(f"❌ Error crítico: {e}")
    finally:
        if automatizacion:
            automatizacion.cerrar_app()


if __name__ == "__main__":
    main()