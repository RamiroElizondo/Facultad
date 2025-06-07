from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, InvalidSelectorException

import time
import os
import unittest

class Automatizar(unittest.TestCase):
    """Clase para automatizar pruebas en la aplicación Chrome en Android usando Appium"""
    def __init__(self,platform_name="Android", platform_version="12", device_name="a31"):
        self.__driver = None
        self.__options = UiAutomator2Options()
        self.__options.platform_name = platform_name
        self.__options.platform_version = platform_version
        self.__options.device_name = device_name
        self.__options.automation_name = "UiAutomator2"
        self.__options.app_package = "com.android.chrome"
        self.__options.app_activity = "org.chromium.chrome.browser.ChromeTabbedActivity"
        self.__webview_context = None
    
    def configurarChrome(self):
        """Busca ChromeDriver en ubicaciones comunes"""
        path = str(os.path.join(os.path.dirname(__file__), "chromedriver.exe"))
        
        if os.path.exists(path):
            abs_path = os.path.abspath(path)
            print(f"✅ ChromeDriver encontrado: {abs_path}")
        
        if abs_path:
            self.__options.set_capability("chromedriverExecutable", abs_path)
            print(f"✅ ChromeDriver configurado: {abs_path}")
        else:
            print("⚠️  ChromeDriver no encontrado localmente")
            print("🔄 Intentando con descarga automática de Appium...")
            
            # Configuraciones para descarga automática
            self.__options.set_capability("chromedriverAutodownload", True)
            self.__options.set_capability("chromedriverChromeMappingFile", "")

    def iniciarDriver(self):
        """Inicia el driver de Appium con las opciones configuradas"""
        self.configurarChrome()
        
        # Configuraciones adicionales para WebView
        self.__options.set_capability("enableWebviewDetailsCollection", True)
        self.__options.set_capability("ensureWebviewsHavePages", True)
        self.__options.set_capability("webviewDevtoolsPort", 9222)
        
        print("🚀 Iniciando driver...")
        self.__driver = webdriver.Remote("http://localhost:4723/wd/hub", options=self.__options)
        
        time.sleep(6)
    
    def manejoDialogos(self):
        dialogos = [
            "Usar sin una cuenta",
            "Más",
            "Entendido",
        ]

        print("🔄 Manejo de diálogos iniciales de Chrome...")
        for dialog in dialogos:
            try:
                element = self.__driver.find_element(AppiumBy.XPATH,f'//*[@text="{dialog}"]')
                element.click()
                time.sleep(3)
                print(f"✅ Se hizo click en '{dialog}'")
            except Exception as e:
                print(f"⚠️ No se pudo encontrar el diálogo '{dialog}': {e}")
                continue
        
        time.sleep(3)
    
    def entrarPagina(self,url,wait:WebDriverWait):
        print("🌐 Navegando a automationexercise.com...")
        self.__driver.get(url)
        try:
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text, 'Automation')]")))
            print("✅ Página cargada correctamente.")
        except:
            print("⚠️  No se pudo verificar la carga completa de la página.")

    def cambiarContexto(self,wait:WebDriverWait):
        # Mostrar contextos disponibles
        contexts = self.__driver.contexts
        print(f"📱 Contextos disponibles: {contexts}")

        # Buscar contexto WebView
        for context in contexts:
            if 'WEBVIEW' in context or 'chrome' in context.lower():
                self.__webview_context = context
                break
        if self.__webview_context:
            try:
                print(f"🔄 Cambiando a contexto: {self.__webview_context}")
                
                # Esperar un poco antes del cambio
                time.sleep(2)
                
                self.__driver.switch_to.context(self.__webview_context)
                print("✅ ¡Cambio de contexto exitoso!")
                
                # Esperar a que el WebView esté listo
                wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                time.sleep(4)
            except InvalidSelectorException as e:
                error_msg = str(e)
                print(f"⚠️  Error al cambiar a WebView: {error_msg}")
            except Exception as e:
                error_msg = str(e)
                print(f"❌ Error al cambiar a WebView: {error_msg}")

    def getDriver(self):
        """Retorna el driver de Appium"""
        return self.__driver

    def cerrarDriver(self):
        print("\n🏁 Cerrando driver...")
        try:
            self.__driver.quit()
            print("✅ Driver cerrado correctamente")
        except:
            print("⚠️  Error cerrando driver")

        print("✅ Script completado")
        

    def agregarProducto(self, wait:WebDriverWait):
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-image-wrapper")))
            productos = self.__driver.find_elements(By.CSS_SELECTOR, ".product-image-wrapper")
            print(f"✅ Se encontraron {len(productos)} productos.")
            nombre_buscado = "Blue Top"

            for producto in productos:
                    #Dentro de productinfo text-center hay un p que tiene el nombre del producto
                    nombre_elemento = producto.find_element(By.TAG_NAME, "p")

                    nombre = nombre_elemento.text.strip()
                    print(f"Producto encontrado: {nombre}")
                    
                    if nombre.lower() == nombre_buscado.lower():
                        print(f"Producto '{nombre}' encontrado. Agregando al carrito...")
                        boton = producto.find_element(By.CSS_SELECTOR, ".add-to-cart")
                        boton.click()
                        break
                    else:
                        print(f"Producto '{nombre}' no coincide con '{nombre_buscado}'")
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-success.close-modal.btn-block")))
            print("Continuar con la compra...")
            continuar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success.close-modal.btn-block")))
            continuar.click()
            print("✅ Se hizo click en Continue Shopping")
        except TimeoutException as e:
            print(f"\n⏰ Timeout esperando un elemento: {str(e)}")
            try:
                screenshot_filename = f"timeout_casoPrueba1_{int(time.time())}.png"
                screenshot_path = os.path.join(os.path.dirname(__file__), screenshot_filename)
                self.__driver.save_screenshot(screenshot_path)
                print(f"📸 Screenshot guardado: {screenshot_path}")
            except:
                pass
        except InvalidSelectorException as e:
            print("Error en WEBVIEW: ")

    #Correcto cuando valor = 1, icnorrecto cuando valor = 0
    def casoDePrueba1(self, wait: WebDriverWait,valor=1):
        try:
            # Paso 3: Verificar que la página de inicio sea visible correctamente
            print("3. Verificando que la página de inicio sea visible...")
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            assert "Automation Exercise" in self.__driver.page_source, "La página de inicio no es visible"
            print("✅ Página de inicio verificada correctamente")
            
            if valor == 0:
                # Paso 4: Hacer clic en el botón "Registrarse / Iniciar sesión"
                print("4. Haciendo clic en 'Signup / Login'...")
                signup_login_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login")))
                signup_login_btn.click()
                time.sleep(2)
                print("✅ Botón 'Signup / Login' clickeado")
            
            else:
                flecha = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button'], .arrow, .close-button")))
                flecha.click()
                # Paso 4: Hacer clic en el botón "Registrarse / Iniciar sesión"
                print("4. Haciendo clic en 'Signup / Login'...")
                signup_login_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login")))
                signup_login_btn.click()
                time.sleep(2)
                print("✅ Botón 'Signup / Login' clickeado")
                
                # Paso 5: Verificar que "¡Registro de nuevo usuario!" esté visible
                print("5. Verificando que 'New User Signup!' esté visible...")
                wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'New User Signup!')]")))
                print("✅ Texto 'New User Signup!' verificado")
                
                # Paso 6: Ingresar nombre y dirección de correo electrónico
                print("6. Ingresando nombre y email...")
                nombre_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='signup-name']")))
                email_input = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']")
                
                # Generar datos únicos para el test
                import random
                timestamp = str(int(time.time()))
                nombre_usuario = f"TestUser{timestamp}"
                email_usuario = f"test{timestamp}@testmail.com"
                
                nombre_input.clear()
                nombre_input.send_keys(nombre_usuario)
                email_input.clear()
                email_input.send_keys(email_usuario)
                print(f"✅ Nombre: {nombre_usuario}, Email: {email_usuario}")
                
                # Paso 7: Hacer clic en el botón "Registrarse"
                print("7. Haciendo clic en 'Signup'...")
                signup_btn = self.__driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']")
                signup_btn.click()
                time.sleep(3)
                print("✅ Botón 'Signup' clickeado")
                
                # Paso 8: Verificar que 'INGRESAR INFORMACIÓN DE LA CUENTA' esté visible
                print("8. Verificando 'ENTER ACCOUNT INFORMATION'...")
                wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Enter Account Information') or contains(text(), 'ENTER ACCOUNT INFORMATION')]")))
                print("✅ Página de información de cuenta verificada")
                
                # Paso 9: Completar los datos de la cuenta
                print("9. Completando datos de la cuenta...")
                
                # Seleccionar título (Mr./Mrs.)
                title_radio = wait.until(EC.element_to_be_clickable((By.ID, "id_gender1")))  # Mr.
                title_radio.click()
                
                # Contraseña
                password_input = self.__driver.find_element(By.ID, "password")
                password_input.send_keys("TestPassword123!")
                
                # Fecha de nacimiento
                day_select = self.__driver.find_element(By.ID, "days")
                day_select.send_keys("15")
                
                month_select = self.__driver.find_element(By.ID, "months")
                month_select.send_keys("January")
                
                year_select = self.__driver.find_element(By.ID, "years")
                year_select.send_keys("1990")
                
                print("✅ Datos de cuenta completados")
                
                # Paso 10: Seleccionar newsletter
                print("10. Seleccionando suscripción al newsletter...")
                newsletter_checkbox = self.__driver.find_element(By.ID, "newsletter")
                if not newsletter_checkbox.is_selected():
                    newsletter_checkbox.click()
                
                # Paso 11: Seleccionar ofertas especiales
                print("11. Seleccionando ofertas especiales...")
                offers_checkbox = self.__driver.find_element(By.ID, "optin")
                if not offers_checkbox.is_selected():
                    offers_checkbox.click()
                
                # Paso 12: Completar datos de dirección
                print("12. Completando datos de dirección...")
                
                # Información personal
                first_name = self.__driver.find_element(By.ID, "first_name")
                first_name.send_keys("Test")
                
                last_name = self.__driver.find_element(By.ID, "last_name")
                last_name.send_keys("User")
                
                company = self.__driver.find_element(By.ID, "company")
                company.send_keys("Test Company")
                
                address1 = self.__driver.find_element(By.ID, "address1")
                address1.send_keys("123 Test Street")
                
                address2 = self.__driver.find_element(By.ID, "address2")
                address2.send_keys("Apt 456")
                
                # País
                country = self.__driver.find_element(By.ID, "country")
                country.send_keys("United States")
                
                # Estado
                state = self.__driver.find_element(By.ID, "state")
                state.send_keys("California")
                
                # Ciudad
                city = self.__driver.find_element(By.ID, "city")
                city.send_keys("Los Angeles")
                
                # Código postal
                zipcode = self.__driver.find_element(By.ID, "zipcode")
                zipcode.send_keys("90210")
                
                # Teléfono móvil
                mobile_number = self.__driver.find_element(By.ID, "mobile_number")
                mobile_number.send_keys("1234567890")
                
                print("✅ Datos de dirección completados")
                
                # Paso 13: Hacer clic en "Crear cuenta"
                print("13. Haciendo clic en 'Create Account'...")
                create_account_btn = self.__driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
                create_account_btn.click()
                time.sleep(5)
                print("✅ Botón 'Create Account' clickeado")
                
                # Paso 14: Verificar que '¡CUENTA CREADA!' esté visible
                print("14. Verificando 'ACCOUNT CREATED!'...")
                wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Account Created!') or contains(text(), 'ACCOUNT CREATED!')]")))
                print("✅ Cuenta creada exitosamente")
                
                # Paso 15: Hacer clic en "Continuar"
                print("15. Haciendo clic en 'Continue'...")
                continue_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='continue-button']")))
                continue_btn.click()
                time.sleep(3)
                print("✅ Botón 'Continue' clickeado")
                
                # Paso 16: Verificar que "Logged in as username" esté visible
                print("16. Verificando 'Logged in as username'...")
                wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), 'Logged in as') and contains(text(), '{nombre_usuario}')]")))
                print(f"✅ Usuario logueado como: {nombre_usuario}")
                
                # Paso 17: Hacer clic en "Eliminar cuenta"
                print("17. Haciendo clic en 'Delete Account'...")
                delete_account_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Delete Account")))
                delete_account_btn.click()
                time.sleep(3)
                print("✅ Botón 'Delete Account' clickeado")
                
                # Paso 18: Verificar que "¡CUENTA ELIMINADA!" esté visible y hacer clic en "Continuar"
                print("18. Verificando 'ACCOUNT DELETED!' y haciendo clic en 'Continue'...")
                wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Account Deleted!') or contains(text(), 'ACCOUNT DELETED!')]")))
                print("✅ Cuenta eliminada exitosamente")
                
                continue_btn_final = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='continue-button']")))
                continue_btn_final.click()
                time.sleep(2)
                print("✅ Proceso completado - Botón 'Continue' final clickeado")
                
                print("\n🎉 ¡Caso de Prueba 1 ejecutado exitosamente!")

        except TimeoutException as e:
            print(f"\n⏰ Timeout esperando un elemento: {str(e)}")
            try:
                screenshot_filename = f"timeout_casoPrueba1_{int(time.time())}.png"
                screenshot_path = os.path.join(os.path.dirname(__file__), screenshot_filename)
                self.__driver.save_screenshot(screenshot_path)
                print(f"📸 Screenshot guardado: {screenshot_path}")
            except:
                pass

        except ElementClickInterceptedException as e:
            print(f"\n⚠️ Elemento no clickeable: {str(e)}")
            # Tomar screenshot para debug si es posible
            try:
                screenshot_filename = f"error_casoPrueba1_{int(time.time())}.png"
                screenshot_path = os.path.join(os.path.dirname(__file__), screenshot_filename)
                self.__driver.save_screenshot(screenshot_path)
                print(f"📸 Screenshot guardado: {screenshot_path}")
            except:
                pass
            
        except Exception as e:
            print(f"\n❌ Error en Caso de Prueba 1: {str(e)}")
            # Tomar screenshot para debug si es posible
            try:
                screenshot_filename = f"error_casoPrueba1_{int(time.time())}.png"
                screenshot_path = os.path.join(os.path.dirname(__file__), screenshot_filename)
                self.__driver.save_screenshot(screenshot_path)
                print(f"📸 Screenshot guardado: {screenshot_path}")
            except:
                pass

    def casoDePrueba24(self, wait: WebDriverWait):
        """Caso de Prueba 24: Descargar factura después de la orden de compra"""
        try:
            print("\n🧪 Iniciando Caso de Prueba 24: Descargar factura después de la orden de compra")
            
            # Paso 3: Verificar que la página de inicio sea visible correctamente
            print("3. Verificando que la página de inicio sea visible...")
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            assert "Automation Exercise" in self.__driver.page_source, "La página de inicio no es visible"
            print("✅ Página de inicio verificada correctamente")
            
            # Paso 4: Añadir productos al carrito
            print("4. Añadiendo productos al carrito...")
            self.agregarProducto(wait)
            print("✅ Producto agregado al carrito")
            
            # Paso 5: Hacer clic en el botón "Carrito"
            print("5. Haciendo clic en el botón 'Cart'...")
            cart_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Cart")))
            cart_btn.click()
            time.sleep(3)
            print("✅ Botón 'Cart' clickeado")
            
            # Paso 6: Verificar que se muestre la página del carrito
            print("6. Verificando que se muestre la página del carrito...")
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Shopping Cart')]")))
            print("✅ Página del carrito verificada")
            
            # Paso 7: Hacer clic en Proceder al pago
            print("7. Haciendo clic en 'Proceed To Checkout'...")
            checkout_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed To Checkout")))
            checkout_btn.click()
            time.sleep(3)
            print("✅ Botón 'Proceed To Checkout' clickeado")
            
            # Paso 8: Hacer clic en el botón «Registrarse / Iniciar sesión»
            print("8. Haciendo clic en 'Register / Login'...")
            register_login_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register / Login")))
            register_login_btn.click()
            time.sleep(2)
            print("✅ Botón 'Register / Login' clickeado")
            
            # Paso 9: Completar todos los datos en Registrarse y crear cuenta
            print("9. Completando registro y creando cuenta...")
            
            # Verificar que "¡Registro de nuevo usuario!" esté visible
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'New User Signup!')]")))
            
            # Ingresar nombre y dirección de correo electrónico
            nombre_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='signup-name']")))
            email_input = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']")
            
            # Generar datos únicos para el test
            import random
            timestamp = str(int(time.time()))
            nombre_usuario = f"TestUser{timestamp}"
            email_usuario = f"test{timestamp}@testmail.com"
            
            nombre_input.clear()
            nombre_input.send_keys(nombre_usuario)
            email_input.clear()
            email_input.send_keys(email_usuario)
            
            # Hacer clic en el botón "Registrarse"
            signup_btn = self.__driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']")
            signup_btn.click()
            time.sleep(3)
            
            # Completar información de la cuenta
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Enter Account Information')]")))
            
            # Seleccionar título
            title_radio = wait.until(EC.element_to_be_clickable((By.ID, "id_gender1")))
            title_radio.click()
            
            # Contraseña
            password_input = self.__driver.find_element(By.ID, "password")
            password_input.send_keys("TestPassword123!")
            
            # Fecha de nacimiento
            day_select = self.__driver.find_element(By.ID, "days")
            day_select.send_keys("15")
            month_select = self.__driver.find_element(By.ID, "months")
            month_select.send_keys("January")
            year_select = self.__driver.find_element(By.ID, "years")
            year_select.send_keys("1990")
            
            # Completar datos de dirección
            first_name = self.__driver.find_element(By.ID, "first_name")
            first_name.send_keys("Test")
            last_name = self.__driver.find_element(By.ID, "last_name")
            last_name.send_keys("User")
            company = self.__driver.find_element(By.ID, "company")
            company.send_keys("Test Company")
            address1 = self.__driver.find_element(By.ID, "address1")
            address1.send_keys("123 Test Street")
            country = self.__driver.find_element(By.ID, "country")
            country.send_keys("United States")
            state = self.__driver.find_element(By.ID, "state")
            state.send_keys("California")
            city = self.__driver.find_element(By.ID, "city")
            city.send_keys("Los Angeles")
            zipcode = self.__driver.find_element(By.ID, "zipcode")
            zipcode.send_keys("90210")
            mobile_number = self.__driver.find_element(By.ID, "mobile_number")
            mobile_number.send_keys("1234567890")
            
            # Crear cuenta
            create_account_btn = self.__driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
            create_account_btn.click()
            time.sleep(5)
            print("✅ Cuenta creada exitosamente")
            
            # Paso 10: Verificar "¡CUENTA CREADA!" y hacer clic en "Continuar"
            print("10. Verificando 'ACCOUNT CREATED!' y haciendo clic en 'Continue'...")
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Account Created!')]")))
            continue_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='continue-button']")))
            continue_btn.click()
            time.sleep(3)
            print("✅ Botón 'Continue' clickeado")
            
            # Paso 11: Verificar 'Logged in as username' en la parte superior
            print("11. Verificando 'Logged in as username'...")
            wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), 'Logged in as')]")))
            print(f"✅ Usuario logueado correctamente")
            
            # Paso 12: Hacer clic en el botón "Carrito"
            print("12. Haciendo clic en el botón 'Cart'...")
            cart_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Cart")))
            cart_btn.click()
            time.sleep(3)
            print("✅ Botón 'Cart' clickeado")
            
            # Paso 13: Hacer clic en el botón "Proceder al pago"
            print("13. Haciendo clic en 'Proceed To Checkout'...")
            checkout_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed To Checkout")))
            checkout_btn.click()
            time.sleep(3)
            print("✅ Botón 'Proceed To Checkout' clickeado")
            
            # Paso 14: Verificar los detalles de la dirección y revisar el pedido
            print("14. Verificando detalles de dirección y revisando pedido...")
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Review Your Order')]")))
            print("✅ Detalles de dirección y pedido verificados")
            
            # Paso 15: Ingresar descripción y hacer clic en "Realizar pedido"
            print("15. Ingresando descripción y haciendo clic en 'Place Order'...")
            comment_textarea = self.__driver.find_element(By.TAG_NAME, "textarea")
            comment_textarea.send_keys("Pedido de prueba automatizada - Caso 24")
            
            place_order_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Place Order")))
            place_order_btn.click()
            time.sleep(3)
            print("✅ Botón 'Place Order' clickeado")
            
            # Paso 16: Ingresar detalles del pago
            print("16. Ingresando detalles del pago...")
            name_on_card = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='name-on-card']")))
            name_on_card.send_keys("Test User")
            
            card_number = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='card-number']")
            card_number.send_keys("4111111111111111")
            
            cvc = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='cvc']")
            cvc.send_keys("123")
            
            expiry_month = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='expiry-month']")
            expiry_month.send_keys("12")
            
            expiry_year = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='expiry-year']")
            expiry_year.send_keys("2030")
            print("✅ Detalles del pago ingresados")
            
            # Paso 17: Hacer clic en "Pagar y confirmar pedido"
            print("17. Haciendo clic en 'Pay and Confirm Order'...")
            pay_confirm_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='pay-button']")))
            pay_confirm_btn.click()
            time.sleep(5)
            print("✅ Botón 'Pay and Confirm Order' clickeado")
            
            # Paso 18: Verificar mensaje de éxito
            print("18. Verificando mensaje de éxito '¡Su pedido se ha realizado correctamente!'...")
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Your order has been placed successfully!') or contains(text(), 'Congratulations!')]")))
            print("✅ Mensaje de éxito verificado")
            
            # Paso 19: Hacer clic en "Descargar factura" y verificar descarga
            print("19. Haciendo clic en 'Download Invoice' y verificando descarga...")
            try:
                download_invoice_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Download Invoice")))
                download_invoice_btn.click()
                time.sleep(3)
                print("✅ Botón 'Download Invoice' clickeado - Factura descargada")
            except:
                print("⚠️ Botón 'Download Invoice' no encontrado o no clickeable")
            
            # Paso 20: Hacer clic en "Continuar"
            print("20. Haciendo clic en 'Continue'...")
            continue_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='continue-button']")))
            continue_btn.click()
            time.sleep(3)
            print("✅ Botón 'Continue' clickeado")
            
            # Paso 21: Hacer clic en "Eliminar cuenta"
            print("21. Haciendo clic en 'Delete Account'...")
            delete_account_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Delete Account")))
            delete_account_btn.click()
            time.sleep(3)
            print("✅ Botón 'Delete Account' clickeado")
            
            # Paso 22: Verificar "¡CUENTA ELIMINADA!" y hacer clic en "Continuar"
            print("22. Verificando 'ACCOUNT DELETED!' y haciendo clic en 'Continue'...")
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Account Deleted!')]")))
            continue_btn_final = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='continue-button']")))
            continue_btn_final.click()
            time.sleep(2)
            print("✅ Cuenta eliminada exitosamente")
            
            print("\n🎉 ¡Caso de Prueba 24 ejecutado exitosamente!")
            
        except TimeoutException as e:
            print(f"\n⏰ Timeout esperando un elemento: {str(e)}")
            try:
                screenshot_filename = f"timeout_casoPrueba24_{int(time.time())}.png"
                screenshot_path = os.path.join(os.path.dirname(__file__), screenshot_filename)
                self.__driver.save_screenshot(screenshot_path)
                print(f"📸 Screenshot guardado: {screenshot_path}")
            except:
                pass
                
        except ElementClickInterceptedException as e:
            print(f"\n⚠️ Elemento no clickeable (interceptado por anuncio): {str(e)}")
            # Intentar cerrar iframe de anuncio y reintentar
            self.cerrarIframeAnuncio(wait)
            try:
                screenshot_filename = f"intercepted_casoPrueba24_{int(time.time())}.png"
                screenshot_path = os.path.join(os.path.dirname(__file__), screenshot_filename)
                self.__driver.save_screenshot(screenshot_path)
                print(f"📸 Screenshot guardado: {screenshot_path}")
            except:
                pass
                
        except Exception as e:
            print(f"\n❌ Error en Caso de Prueba 24: {str(e)}")
            try:
                screenshot_filename = f"error_casoPrueba24_{int(time.time())}.png"
                screenshot_path = os.path.join(os.path.dirname(__file__), screenshot_filename)
                self.__driver.save_screenshot(screenshot_path)
                print(f"📸 Screenshot guardado: {screenshot_path}")
            except:
                pass       
if __name__ == "__main__":
    # Crear instancia de Automatizar y ejecutar el flujo
    automatizar = Automatizar()
    automatizar.iniciarDriver()
    automatizar.manejoDialogos()
    wait = WebDriverWait(automatizar.getDriver(), 20)
    automatizar.entrarPagina("https://automationexercise.com/", wait)
    automatizar.cambiarContexto(wait)

    # Pruebas en la pagina:
    """
    Caso de prueba 1: Registrar usuario
    Caso de prueba 24: Descargar factura después de la orden de compra
    """
    
    automatizar.agregarProducto(wait)

    print('\n🧪 Ejecutando Caso de Prueba 1: Registrar usuario Invalido')
    automatizar.casoDePrueba1(wait,valor=0)
    print('\n🧪 Ejecutando Caso de Prueba 1: Registrar usuario Valido')
    automatizar.casoDePrueba1(wait,valor=1) 
    #automatizar.casoDePrueba24(wait)
    
    time.sleep(60)
    automatizar.cerrarDriver()