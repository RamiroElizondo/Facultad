from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "12"
options.device_name = "a31"
options.automation_name = "UiAutomator2"
options.app_package = "com.android.chrome"
options.app_activity = "com.google.android.apps.chrome.Main"
options.auto_grant_permissions = True
options.optional_intent_arguments = "-d https://automationexercise.com"
options.new_command_timeout = 300  # evita que se cierre la sesión por inactividad

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

time.sleep(5)

# Interacciones con la interfaz inicial
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

# Esperar a que cargue la web
wait = WebDriverWait(driver, 20)
try:
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text, 'Automation')]")))
    print("Página cargada correctamente.")
except:
    print("No se pudo verificar la carga de la página.")

# Mantener la sesión viva por 60 segundos
time.sleep(60)

driver.quit()
