from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
import requests
import zipfile
import os
import platform

def get_chrome_version():
    """Obtiene la versión de Chrome del dispositivo"""
    try:
        # Comando ADB para obtener la versión de Chrome
        result = subprocess.run(['adb', 'shell', 'dumpsys', 'package', 'com.android.chrome'], 
                              capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if 'versionName' in line:
                version = line.split('=')[1].strip()
                return version
    except:
        pass
    return None

def download_chromedriver(version):
    """Descarga el ChromeDriver compatible"""
    try:
        # URL base para descargar ChromeDriver
        base_url = "https://chromedriver.storage.googleapis.com"
        
        # Para versiones 115+, usar la nueva URL
        if int(version.split('.')[0]) >= 115:
            base_url = "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json"
            # Lógica para versiones nuevas (más compleja)
            print(f"Chrome version {version} requires newer ChromeDriver download method")
            return None
        
        # Obtener la versión exacta del ChromeDriver
        version_url = f"{base_url}/LATEST_RELEASE_{version.split('.')[0]}"
        response = requests.get(version_url)
        chromedriver_version = response.text.strip()
        
        # Determinar la plataforma
        system = platform.system().lower()
        if system == "windows":
            platform_name = "win32"
            executable_name = "chromedriver.exe"
        elif system == "darwin":
            platform_name = "mac64"
            executable_name = "chromedriver"
        else:
            platform_name = "linux64"
            executable_name = "chromedriver"
        
        # Descargar ChromeDriver
        download_url = f"{base_url}/{chromedriver_version}/chromedriver_{platform_name}.zip"
        print(f"Descargando ChromeDriver desde: {download_url}")
        
        response = requests.get(download_url)
        with open("chromedriver.zip", "wb") as f:
            f.write(response.content)
        
        # Extraer el archivo
        with zipfile.ZipFile("chromedriver.zip", 'r') as zip_ref:
            zip_ref.extractall(".")
        
        # Limpiar
        os.remove("chromedriver.zip")
        
        print(f"ChromeDriver descargado exitosamente: {executable_name}")
        return executable_name
        
    except Exception as e:
        print(f"Error descargando ChromeDriver: {e}")
        return None

# Configuración de opciones mejorada
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "12"
options.device_name = "a31"
options.automation_name = "UiAutomator2"
options.app_package = "com.android.chrome"
options.app_activity = "org.chromium.chrome.browser.ChromeTabbedActivity"  # Corregido
options.auto_grant_permissions = True
options.no_reset = True  # Evita resetear la app

# Configuraciones adicionales para WebView
options.set_capability("chromedriverExecutable", "chromedriver.exe")  # Especifica el path del ChromeDriver
options.set_capability("enableWebviewDetailsCollection", True)
options.set_capability("webviewDevtoolsPort", 9222)
options.set_capability("ensureWebviewsHavePages", True)
options.set_capability("nativeWebScreenshot", True)

# Obtener versión de Chrome
chrome_version = get_chrome_version()
if chrome_version:
    print(f"Versión de Chrome detectada: {chrome_version}")
    
    # Intentar descargar ChromeDriver compatible
    chromedriver_path = download_chromedriver(chrome_version)
    if chromedriver_path:
        options.set_capability("chromedriverExecutable", os.path.abspath(chromedriver_path))

try:
    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    print("✅ Driver inicializado correctamente")

    time.sleep(5)  # Wait for the app to load

    # Manejo de diálogos iniciales de Chrome
    dialog_texts = [
        "Usar sin una cuenta",
        "Sí, acepto", 
        "Más",
        "Entendido",
        "No, gracias",
        "Aceptar"
    ]
    
    for dialog_text in dialog_texts:
        try:
            element = driver.find_element(AppiumBy.XPATH, f"//*[@text='{dialog_text}']")
            element.click()
            time.sleep(1)
            print(f"✅ Clicked en: {dialog_text}")
        except:
            continue

    time.sleep(3)
    
    # Navegar a la página
    print("Navegando a automationexercise.com...")
    driver.get("https://automationexercise.com/")

    # Esperar a que la página cargue
    wait = WebDriverWait(driver, 30)
    try:
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text, 'Automation')]")))
        print("✅ Página cargada correctamente.")
    except:
        print("⚠️  No se pudo verificar la carga de la página completamente.")

    # Mostrar contextos disponibles
    contexts = driver.contexts
    print(f"Contextos disponibles: {contexts}")

    # Cambiar a WebView con manejo de errores mejorado
    webview_context = None
    for context in contexts:
        if 'WEBVIEW' in context or 'CHROME' in context:
            webview_context = context
            break
    
    if webview_context:
        try:
            print(f"Cambiando a contexto: {webview_context}")
            driver.switch_to.context(webview_context)
            print("✅ Cambio de contexto exitoso")
            
            # Esperar a que los elementos web estén disponibles
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            
            # Buscar productos usando diferentes selectores
            selectors_to_try = [
                (By.CLASS_NAME, "product-image-wrapper"),
                (By.CSS_SELECTOR, ".product-image-wrapper"),
                (By.CSS_SELECTOR, "[class*='product']"),
                (By.TAG_NAME, "img")
            ]
            
            productos = []
            for selector_type, selector_value in selectors_to_try:
                try:
                    productos = driver.find_elements(selector_type, selector_value)
                    if productos:
                        print(f"✅ Se encontraron {len(productos)} elementos usando {selector_type}: {selector_value}")
                        break
                except Exception as e:
                    print(f"⚠️  No se encontraron elementos con {selector_type}: {selector_value}")
                    continue
            
            if not productos:
                print("⚠️  No se encontraron productos. Verificando el HTML...")
                # Obtener el HTML para debug
                html_source = driver.page_source
                print(f"Título de la página: {driver.title}")
                print(f"URL actual: {driver.current_url}")
                
        except Exception as e:
            print(f"❌ Error al cambiar a WebView: {e}")
            print("Intentando alternativas...")
            
            # Alternativa 1: Esperar más tiempo
            time.sleep(5)
            try:
                driver.switch_to.context(webview_context)
                print("✅ Cambio de contexto exitoso en segundo intento")
            except Exception as e2:
                print(f"❌ Error en segundo intento: {e2}")
                
                # Alternativa 2: Recargar la página
                try:
                    driver.refresh()
                    time.sleep(5)
                    driver.switch_to.context(webview_context)
                    print("✅ Cambio de contexto exitoso después de refresh")
                except Exception as e3:
                    print(f"❌ Error después de refresh: {e3}")
    else:
        print("❌ No se encontró contexto WebView disponible")

except Exception as e:
    print(f"❌ Error general: {e}")
    
finally:
    # Limpiar recursos
    try:
        if 'driver' in locals():
            driver.quit()
        print("✅ Driver cerrado correctamente")
    except:
        pass