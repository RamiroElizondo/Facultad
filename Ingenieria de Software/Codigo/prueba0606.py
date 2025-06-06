from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def find_chromedriver():
    """Busca ChromeDriver en ubicaciones comunes"""
    paths_to_check = [
        "chromedriver.exe",
        "./chromedriver.exe",
        os.path.abspath("chromedriver.exe"),
        "C:/chromedriver/chromedriver.exe",
        "C:/WebDriver/bin/chromedriver.exe"
    ]
    
    for path in paths_to_check:
        if os.path.exists(path):
            abs_path = os.path.abspath(path)
            print(f"✅ ChromeDriver encontrado: {abs_path}")
            return abs_path
    
    return None

options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "12"
options.device_name = "a31"
options.automation_name = "UiAutomator2"
options.app_package = "com.android.chrome"
options.app_activity = "org.chromium.chrome.browser.ChromeTabbedActivity"
options.auto_grant_permissions = True

# 🔧 CONFIGURACIÓN MEJORADA DEL CHROMEDRIVER
chromedriver_path = find_chromedriver()

print(chromedriver_path)
if chromedriver_path:
    options.set_capability("chromedriverExecutable", chromedriver_path)
    print(f"✅ ChromeDriver configurado: {chromedriver_path}")
else:
    print("⚠️  ChromeDriver no encontrado localmente")
    print("🔄 Intentando con descarga automática de Appium...")
    
    # Configuraciones para descarga automática
    options.set_capability("chromedriverAutodownload", True)
    options.set_capability("chromedriverChromeMappingFile", "")

# Configuraciones adicionales para WebView
options.set_capability("enableWebviewDetailsCollection", True)
options.set_capability("ensureWebviewsHavePages", True)
options.set_capability("webviewDevtoolsPort", 9222)

print("🚀 Iniciando driver...")
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

time.sleep(5)  # Wait for the app to load

# Manejo de diálogos iniciales de Chrome
dialog_attempts = [
    "Usar sin una cuenta",
    "Sí, acepto", 
    "Más",
    "Entendido",
    "No gracias",
    "Aceptar",
    "OK"
]

for dialog_text in dialog_attempts:
    try:
        element = driver.find_element(AppiumBy.XPATH, f"//*[@text='{dialog_text}']")
        element.click()
        time.sleep(1)
        print(f"✅ Clicked: {dialog_text}")
    except:
        continue

time.sleep(3)
print("🌐 Navegando a automationexercise.com...")
driver.get("https://automationexercise.com/")

wait = WebDriverWait(driver, 20)
try:
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text, 'Automation')]")))
    print("✅ Página cargada correctamente.")
except:
    print("⚠️  No se pudo verificar la carga completa de la página.")

# Mostrar contextos disponibles
contexts = driver.contexts
print(f"📱 Contextos disponibles: {contexts}")

# Buscar contexto WebView
webview_context = None
for context in contexts:
    if 'WEBVIEW' in context or 'chrome' in context.lower():
        webview_context = context
        break

if webview_context:
    try:
        print(f"🔄 Cambiando a contexto: {webview_context}")
        
        # Esperar un poco antes del cambio
        time.sleep(2)
        
        driver.switch_to.context(webview_context)
        print("✅ ¡Cambio de contexto exitoso!")
        
        # Esperar a que el WebView esté listo
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(2)
        
        print("🔍 Buscando productos...")
        
        # Intentar diferentes selectores para productos
        selectors = [
            (By.CLASS_NAME, "product-image-wrapper"),
            (By.CSS_SELECTOR, ".product-image-wrapper"),
            (By.CSS_SELECTOR, "[class*='product']"),
            (By.CSS_SELECTOR, ".col-sm-4"),
            (By.TAG_NAME, "img")
        ]
        
        productos_encontrados = False
        for selector_type, selector_value in selectors:
            try:
                productos = driver.find_elements(selector_type, selector_value)
                if productos:
                    print(f"✅ Se encontraron {len(productos)} elementos con {selector_type}: '{selector_value}'")
                    productos_encontrados = True
                    break
            except Exception as e:
                continue
        
        if not productos_encontrados:
            print("⚠️  No se encontraron productos específicos")
            print(f"📄 Título de la página: {driver.title}")
            print(f"🔗 URL actual: {driver.current_url}")
        
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Error al cambiar a WebView: {error_msg}")
        
        if "chromedriver binary" in error_msg.lower():
            print("\n💡 SOLUCIÓN:")
            print("1. Ejecuta: python chromedriver_locator.py")
            print("2. O descarga ChromeDriver manualmente de:")
            print("   https://googlechromelabs.github.io/chrome-for-testing/")
            print("3. Guárdalo como 'chromedriver.exe' en tu carpeta de proyecto")
        
else:
    print("❌ No se encontró contexto WebView disponible")
    print("💡 Verifica que Chrome haya cargado completamente la página web")

print("\n🏁 Cerrando driver...")
try:
    driver.quit()
    print("✅ Driver cerrado correctamente")
except:
    print("⚠️  Error cerrando driver")

print("✅ Script completado")