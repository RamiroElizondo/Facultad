from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, InvalidSelectorException, WebDriverException
from selenium.webdriver.support.ui import Select
import random

import time
import os
import unittest

class Automatizar(unittest.TestCase):
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
        path = str(os.path.join(os.path.dirname(__file__), "chromedriver.exe"))
        if os.path.exists(path):
            abs_path = os.path.abspath(path)
            self.__options.set_capability("chromedriverExecutable", abs_path)
            print(f"✅ ChromeDriver configurado: {abs_path}")
        else:
            print("⚠️  ChromeDriver no encontrado localmente. Usando autodownload...")
            self.__options.set_capability("chromedriverAutodownload", True)
            self.__options.set_capability("chromedriverChromeMappingFile", "")

    def iniciarDriver(self):
        self.configurarChrome()
        self.__options.set_capability("enableWebviewDetailsCollection", True)
        self.__options.set_capability("ensureWebviewsHavePages", True)
        self.__options.set_capability("webviewDevtoolsPort", 9222)
        self.__options.set_capability("noReset", True)
        print("🚀 Iniciando driver...")
        self.__driver = webdriver.Remote("http://localhost:4723/wd/hub", options=self.__options)
        time.sleep(6)
    
    def manejoDialogos(self):
        dialogos = ["Usar sin una cuenta","Más","Entendido",]
        print("🔄 Manejo de diálogos iniciales de Chrome...")
        for dialog in dialogos:
            try:
                element = self.__driver.find_element(AppiumBy.XPATH,f'//*[@text="{dialog}"]')
                element.click()
                print(f"✅ Se hizo click en '{dialog}'")
                time.sleep(3)
            except Exception:
                print(f"ℹ️ Diálogo '{dialog}' no presente (omitido)")
                continue
        
        time.sleep(3)
    
    def getDriver(self):
        if not self.__driver:
            raise Exception("❌ El driver aún no fue iniciado. Llamá a iniciarDriver primero.")
        try:
            print("🔄 Verificando conexión con el driver...")
            print('driver',self.__driver)
            print('holas',self.__driver.current_context)
            print('Hola',self.__driver.current_url)
            self.__driver.current_url
        except WebDriverException as e:
            raise Exception(f"❌ El driver perdió conexión con el navegador: {e}")
        return self.__driver
    
    def entrarPagina(self,url):
        wait = WebDriverWait(automatizar.getDriver(), 20)
        print("🌐 Navegando a automationexercise.com...")
        print(self.getDriver())
        self.__driver.get(url)
        try:
            time.sleep(7)
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text, 'Automation')]")))
            print("✅ Página cargada correctamente.")
        except:
            print("⚠️  No se pudo verificar la carga completa de la página.")
        finally:
            return self.__driver.page_source

    def cambiarContexto(self):
        wait = WebDriverWait(automatizar.getDriver(), 20)
        # Mostrar contextos disponibles
        contexts = self.__driver.contexts
        print(f"📱 Contextos disponibles: {contexts}")

        if len(contexts) == 1 and contexts[0] == "NATIVE_APP":
            print("⚠️ Solo hay un contexto disponible: NATIVE_APP. No se puede cambiar a WebView.")
            raise Exception("No hay contexto WebView disponible. Asegúrate de que la aplicación esté configurada correctamente para WebView.")

        # Buscar contexto WebView
        for context in contexts:
            if 'WEBVIEW' in context or 'chrome' in context.lower():
                self.__webview_context = context
                break
        if self.__webview_context:
            try:
                print(f"🔄 Cambiando a contexto: {self.__webview_context}")
                
                # Esperar un poco antes del cambio
                time.sleep(3)
                print("Esperando a que el WebView esté listo...")
                self.__driver.switch_to.context(self.__webview_context)
                print("✅ ¡Cambio de contexto exitoso!")
                
                # Esperar a que el WebView esté listo
                wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                print("El contexto actual es:", self.__webview_context)
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
        
    def cerrarIframeAnuncio(self):
        """Cierra el iframe de anuncio o simula cerrar el contenedor que lo incluye"""
        try:
            print("🔄 Buscando iframe de anuncio...")
            print("Contexto actual:", self.__driver.current_context)
            # Esperar iframes
            iframes = self.__driver.find_elements(By.TAG_NAME, "iframe")
            
            print(f"🔍 {len(iframes)} iframe(s) encontrados")

            for iframe in iframes:
                iframe_id = iframe.get_attribute("id") or ""
                src = iframe.get_attribute("src") or ""
                if "aswift" in iframe_id or "google" in iframe_id or "ads" in src:
                    try:
                        self.__driver.execute_script("arguments[0].style.display = 'none';", iframe)
                        print(f"✅ Iframe ocultado (id: {iframe_id})")
                    except Exception as ocultar_error:
                        print(f"⚠️ No se pudo ocultar iframe {iframe_id}: {ocultar_error}")

            # Intentar simular clic en la flecha (íconos de colapso o cierre)
            posibles_flechas = self.__driver.find_elements(By.CSS_SELECTOR, "[aria-label*='cerrar'], [aria-label*='close'], button, div[role='button']")
            for flecha in posibles_flechas:
                try:
                    label = flecha.get_attribute("aria-label") or ""
                    if "cerrar" in label.lower() or "close" in label.lower():
                        flecha.click()
                        print("✅ Flecha de cierre clickeada")
                        time.sleep(1)
                        return True
                except Exception as e:
                    print(f"⚠️ No se pudo clickear flecha: {e}")
                    continue

            return True

        except Exception as e:
            print(f"❌ Error general al manejar iframes de anuncios: {e}")
            return False

    def verificarDriver(self):
        """Verifica si el driver está activo y en el contexto correcto"""
        try:
            if not self.__driver:
                raise Exception("❌ El driver aún no fue iniciado. Llamá a iniciarDriver primero.")
            print("🔄 Verificando conexión con el driver...")
            print("Estamos en",self.__driver.current_url)
            print("✅ Conexión con el driver verificada")
            print("El contexto actual es:", self.__driver.current_context)
        except WebDriverException as e:
            raise Exception(f"❌ El driver perdió conexión con el navegador: {e}")

    def tomarScreenshot(self, filename):
        """Toma un screenshot del estado actual del driver"""
        try:
            screenshot_path = os.path.join(os.path.dirname(__file__), filename)
            self.__driver.save_screenshot(screenshot_path)
            print(f"📸 Screenshot guardado: {screenshot_path}")
        except Exception as e:
            print(f"❌ Error al tomar screenshot: {e}")

    def agregarProducto(self):
        try:
            self.verificarDriver()
            print("🔄 Buscando productos en la página...")
            wait = WebDriverWait(automatizar.getDriver(), 30)
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-image-wrapper")))
            productos = self.__driver.find_elements(By.CSS_SELECTOR, ".product-image-wrapper")
            print(f"✅ Se encontraron {len(productos)} productos.")
            nombre_buscado = "Printed Off Shoulder Top - White"

            for i,producto in enumerate(productos):
                    y_scroll = i * 300  # o cualquier incremento razonable
                    print(f"📜 Haciendo scroll a {y_scroll}px...")
                    try:
                        self.__driver.execute_script(f"window.scrollTo(0, {y_scroll});")
                    except Exception as e:
                        print(f"⚠️ Error haciendo scroll: {e}")
                    #Dentro de productinfo text-center hay un p que tiene el nombre del producto
                    try:
                        nombre_elemento = producto.find_element(By.TAG_NAME, "p")
                        nombre = nombre_elemento.text.strip()
                        print(f"Producto encontrado: {nombre}")

                        if nombre.lower() == nombre_buscado.lower():
                            print(f"✅ Producto '{nombre}' encontrado. Agregando al carrito...")
                            boton = producto.find_element(By.CSS_SELECTOR, ".add-to-cart")
                            boton.click()
                            break
                        else:
                            print(f"Producto '{nombre}' no coincide con '{nombre_buscado}'")
                    except Exception as e:
                        print(f"⚠️ Error leyendo producto: {e}")
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-success.close-modal.btn-block")))
            print("Continuar con la compra...")
            continuar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success.close-modal.btn-block")))
            continuar.click()
            print("✅ Se hizo click en Continue Shopping")
        except TimeoutException as e:
            print(f"\n⏰ Timeout esperando un elemento: {str(e)}")
            try:
                self.tomarScreenshot(f"timeout_agregarProducto_{int(time.time())}.png")
                self.agregarProducto()
            except:
                pass
        except InvalidSelectorException as e:
            print("Error en WEBVIEW: ")

    def verificarExistenciaAnuncio(self,url):
        url_actual = self.__driver.current_url
        if url != url_actual:
            self.cerrarIframeAnuncio()
        return url_actual

    def scroll_into_view(self, element):
        try:
            self.__driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(0.5)
        except Exception as e:
            print(f"⚠️ Error al hacer scroll hacia el elemento: {e}")

    def casoDePrueba1(self):
        try:
            urlActual = self.__driver.current_url
            wait = WebDriverWait(automatizar.getDriver(), 20)
            # Paso 3: Verificar que la página de inicio sea visible correctamente
            print("3. Verificando que la página de inicio sea visible...")
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            assert "Automation Exercise" in self.__driver.page_source, "La página de inicio no es visible"
            print("✅ Página de inicio verificada correctamente")
            
            # Paso 4: Hacer clic en el botón "Registrarse / Iniciar sesión"
            print("4. Haciendo clic en 'Signup / Login'...")
            signup_login_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login")))
            self.scroll_into_view(signup_login_btn)
            signup_login_btn.click()
            time.sleep(2)
            print("✅ Botón 'Signup / Login' clickeado")
            
            urlActual = self.verificarExistenciaAnuncio(urlActual)

            # Paso 5: Verificar que "¡Registro de nuevo usuario!" esté visible
            print("5. Verificando que 'New User Signup!' esté visible...")
            titulo_signup=wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'New User Signup!')]")))
            self.scroll_into_view(titulo_signup)
            print("✅ Texto 'New User Signup!' verificado")
            
            # Paso 6: Ingresar nombre y dirección de correo electrónico
            print("6. Ingresando nombre y email...")
            nombre_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='signup-name']")))
            email_input = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']")
            self.scroll_into_view(nombre_input)
            
            # Generar datos únicos para el test
            
            timestamp = str(int(time.time()))
            nombre_usuario = f"TestUser{timestamp}"
            email_usuario = f"test{timestamp}@testmail.com"
            
            nombre_input.clear()
            nombre_input.send_keys(nombre_usuario)
            email_input.clear()
            email_input.send_keys(email_usuario)
            print(f"✅ Nombre: {nombre_usuario}, Email: {email_usuario}")
            try:
                actions = ActionChains(self.__driver)
                actions.move_by_offset(10, 10).click().perform()
                print("🖱️ Click simulado con ActionChains en (10,10)")
            except Exception as e:
                print(f"⚠️ No se pudo cerrar el teclado con tap: {e}")

            # Paso 7: Hacer clic en el botón "Registrarse"
            print("7. Haciendo clic en 'Signup'...")
            signup_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="signup-button"]')))
            self.scroll_into_view(signup_btn)
            signup_btn.click()

            if self.__driver.current_url == urlActual:
                print("⚠️Realmente no se hizo click'Signup'. Intentando clickeo con JavaScript...")
                self.getDriver().execute_script("arguments[0].click();", signup_btn)


            print("✅ Botón 'Signup' clickeado")
            print("Esperando a que se cargue la página de información de cuenta...")
            time.sleep(6)
            
            
            # Paso 8: Verificar que 'INGRESAR INFORMACIÓN DE LA CUENTA' esté visible
            print("8. Verificando 'ENTER ACCOUNT INFORMATION'...")
            titulo_info = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Enter Account Information') or contains(text(), 'ENTER ACCOUNT INFORMATION')]")))
            self.scroll_into_view(titulo_info)
            print("✅ Página de información de cuenta verificada")
            
            # Paso 9: Completar los datos de la cuenta
            print("9. Completando datos de la cuenta...")
            # Seleccionar título (Mr./Mrs.)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".radio-inline")))
            radiosInlines = self.__driver.find_elements(By.CSS_SELECTOR, ".radio-inline")
            print(f"🔄 Se encontraron {len(radiosInlines)} radios para seleccionar el título")
            for radio in radiosInlines:
                print(f"🔄 Verificando radio: {radio.text}")
                try:
                    radio.find_element(By.TAG_NAME, "input")
                    if "Mr." in radio.text:
                        print("✅ Seleccionando título 'Mr.'")
                        radio.click()
                        break
                    
                except Exception as e:
                    print(f"⚠️ No se pudo seleccionar el título: {e}")
            
            # Contraseña
        
            password_input = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='password']")
            self.scroll_into_view(password_input)
            password_input.send_keys("TestPassword123!")
            try:
                actions = ActionChains(self.__driver)
                actions.move_by_offset(10, 10).click().perform()
                print("🖱️ Click simulado con ActionChains en (10,10)")
            except Exception as e:
                print(f"⚠️ No se pudo cerrar el teclado con tap: {e}")
            
            time.sleep(2)

            # Fecha de nacimiento
            selector_days_div = wait.until(EC.presence_of_element_located((By.ID, "uniform-days")))
            self.scroll_into_view(selector_days_div)
            day_select_el = selector_days_div.find_element(By.TAG_NAME, "select")
            day_select_el.click()
            option_day = day_select_el.find_element(By.CSS_SELECTOR, "option[value='10']")
            option_day.click()

            # Mes
            selector_months_div = self.__driver.find_element(By.ID, "uniform-months")
            self.scroll_into_view(selector_months_div)
            month_select_el = selector_months_div.find_element(By.TAG_NAME, "select")
            month_select_el.click()
            option_month = month_select_el.find_element(By.CSS_SELECTOR, "option[value='5']")
            option_month.click()

            # Año
            selector_years_div = self.__driver.find_element(By.ID, "uniform-years")
            self.scroll_into_view(selector_years_div)
            year_select_el = selector_years_div.find_element(By.TAG_NAME, "select")
            year_select_el.click()
            option_year = year_select_el.find_element(By.CSS_SELECTOR, "option[value='1995']")
            option_year.click()

            print("✅ Fecha de nacimiento seleccionada: 10/5/1995")
            
            print("✅ Datos de cuenta completados")

            titulo_checkboxs = self.__driver.find_element(By.XPATH, "//*[contains(text(), 'Sign Up for our newsletter!') or contains(text(), 'Receive special offers from our partners!')]")
            self.scroll_into_view(titulo_checkboxs)
            # Paso 10 y 11
            print("10. Verificando 'Sign Up for our newsletter!' y 'Receive special offers from our partners!'...")
            checkboxs = self.__driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
            if len(checkboxs) >= 2:
                print("✅ Se encontraron los checkboxs necesarios")
                try:
                    checkboxs[0].click()  # 'Sign Up for our newsletter!'
                    print("✅ Checkbox 'Sign Up for our newsletter!' clickeado")
                except ElementClickInterceptedException:
                    print("⚠️ No se pudo hacer clic en 'Sign Up for our newsletter!'")
                
                try:
                    checkboxs[1].click()  # 'Receive special offers from our partners!'
                    print("✅ Checkbox 'Receive special offers from our partners!' clickeado")
                except ElementClickInterceptedException:
                    print("⚠️ No se pudo hacer clic en 'Receive special offers from our partners!'")
            
            # Paso 12: Completar datos de dirección
            print("12. Completando datos de dirección...")
            
            # Información personal
            first_name = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='first-name']")
            self.scroll_into_view(first_name)
            first_name.send_keys("Test")
            
            last_name = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='last-name']")
            self.scroll_into_view(last_name)
            last_name.send_keys("User")
            
            company = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='company']")
            self.scroll_into_view
            company.send_keys("Test Company")
            
            address1 = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='address']")
            self.scroll_into_view(address1)
            address1.send_keys("123 Test Street")
            
            address2 = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='address2']")
            self.scroll_into_view(address2)
            address2.send_keys("Apt 456")
            
            # País
            contry_select_el = self.__driver.find_element(By.ID, "country")
            self.scroll_into_view(contry_select_el)
            self.scroll_into_view(contry_select_el)
            Select(contry_select_el).select_by_visible_text("United States")
            
            # Estado
            state = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='state']")
            self.scroll_into_view(state)
            state.send_keys("California")
            
            # Ciudad
            city = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='city']")
            self.scroll_into_view(city)
            city.send_keys("Los Angeles")
            
            # Código postal
            zipcode = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='zipcode']")
            self.scroll_into_view(zipcode)
            zipcode.send_keys("90210")
            
            # Teléfono móvil
            mobile_number = self.__driver.find_element(By.CSS_SELECTOR, "input[data-qa='mobile-number']")
            self.scroll_into_view(mobile_number)
            mobile_number.send_keys("1234567890")
            
            print("✅ Datos de dirección completados")
            
            # Paso 13: Hacer clic en "Crear cuenta"
            print("13. Haciendo clic en 'Create Account'...")
            create_account_btn = self.__driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
            self.scroll_into_view(create_account_btn)
            create_account_btn.click()
            if self.__driver.current_url == urlActual:
                print("⚠️ Realmente no se hizo click 'Create Account'. Intentando clickeo con JavaScript...")
                self.getDriver().execute_script("arguments[0].click();", create_account_btn)
            time.sleep(5)
            print("✅ Botón 'Create Account' clickeado")
            urlActual = self.verificarExistenciaAnuncio(urlActual)

            # Paso 14: Verificar que '¡CUENTA CREADA!' esté visible
            print("14. Verificando 'ACCOUNT CREATED!'...")
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Account Created!') or contains(text(), 'ACCOUNT CREATED!')]")))
            print("✅ Cuenta creada exitosamente")
            
            # Paso 15: Hacer clic en "Continuar"
            print("15. Haciendo clic en 'Continue'...")
            continue_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='continue-button']")))
            self.scroll_into_view(continue_btn)
            continue_btn.click()
            time.sleep(3)
            print("✅ Botón 'Continue' clickeado")
            urlActual = self.verificarExistenciaAnuncio(urlActual)
            
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
            urlActual = self.verificarExistenciaAnuncio(urlActual)
            
            # Paso 18: Verificar que "¡CUENTA ELIMINADA!" esté visible y hacer clic en "Continuar"
            print("18. Verificando 'ACCOUNT DELETED!' y haciendo clic en 'Continue'...")
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Account Deleted!') or contains(text(), 'ACCOUNT DELETED!')]")))
            print("✅ Cuenta eliminada exitosamente")
            
            continue_btn_final = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='continue-button']")))
            self.scroll_into_view(continue_btn_final)
            continue_btn_final.click()
            time.sleep(2)
            print("✅ Proceso completado - Botón 'Continue' final clickeado")
            
            print("\n🎉 ¡Caso de Prueba 1 ejecutado exitosamente!")

        except TimeoutException as e:
            print(f"\n⏰ Timeout esperando un elemento: {str(e)}")
            try:
                screenshot_filename = f"timeout_casoPrueba1_{int(time.time())}.png"
                self.tomarScreenshot(screenshot_filename)
                self.casoDePrueba1()
            except:
                pass

        except ElementClickInterceptedException as e:
            print(f"\n⚠️ Elemento no clickeable: {str(e)}")
            # Tomar screenshot para debug si es posible
            try:
                screenshot_filename = f"error_casoPrueba1_{int(time.time())}.png"
                self.tomarScreenshot(screenshot_filename)
                self.casoDePrueba1()
            except:
                pass
            
        except Exception as e:
            print(f"\n❌ Error en Caso de Prueba 1: {str(e)}")
            # Tomar screenshot para debug si es posible
            try:
                screenshot_filename = f"error_casoPrueba1_{int(time.time())}.png"
                self.tomarScreenshot(screenshot_filename)
                print(f"📸 Screenshot guardado: {screenshot_path}")
            except:
                pass

    def casoDePrueba24(self):
        try:
            wait = WebDriverWait(automatizar.getDriver(), 20)
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
    #automatizar.manejoDialogos()
    automatizar.entrarPagina("https://automationexercise.com/")
    automatizar.cambiarContexto()

    # Pruebas en la pagina:
    """
    Caso de prueba 1: Registrar usuario
    Caso de prueba 24: Descargar factura después de la orden de compra
    """
    automatizar.cerrarIframeAnuncio()

    automatizar.agregarProducto()
    print('\n🧪 Ejecutando Caso de Prueba 1: Registrar usuario')
    automatizar.casoDePrueba1() 
    #automatizar.casoDePrueba24()
    
    time.sleep(60)
    automatizar.cerrarDriver()