from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "12"
options.device_name = "a31"
options.automation_name = "UiAutomator2"
options.app_package = "com.android.chrome"
options.app_activity = "com.google.android.apps.chrome.Main"
options.auto_grant_permissions = True

# ⬅️ Línea clave: agregar path a tu chromedriver compatible
options.chromedriver_executable = "C:/Users/Ramiro/chromedriver/chromedriver.exe"

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

time.sleep(5)  # Esperar que cargue la app

# Saltar bienvenida de Chrome
for xpath in [
    "//*[@text='Usar sin una cuenta']",
    "//*[@text='Sí, acepto']",
    "//*[@text='Más']",
    "//*[@text='Entendido']"
]:
    try:
        driver.find_element(AppiumBy.XPATH, xpath).click()
        time.sleep(2)
    except:
        pass

# Ir al sitio deseado
driver.get("https://automationexercise.com/")

wait = WebDriverWait(driver, 20)
try:
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text, 'Automation')]")))
    print("Página cargada correctamente.")
except:
    print("No se pudo verificar la carga de la página.")

# Mostrar contextos y cambiar a WEBVIEW
print(driver.contexts)
driver.switch_to.context('WEBVIEW_chrome')

# Interactuar con el DOM HTML
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-image-wrapper")))
productos = driver.find_elements(By.CLASS_NAME, "product-image-wrapper")
print(f"✅ Se encontraron {len(productos)} productos.")

time.sleep(5)
driver.quit()
