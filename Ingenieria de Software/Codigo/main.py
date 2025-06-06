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
options.app_activity = "org.chromium.chrome.browser.ChromeTabbedActivity t766"
options.auto_grant_permissions = True



driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

time.sleep(5)  # Wait for the app to load

try:
    driver.find_element(AppiumBy.XPATH, "//*[@text='Usar sin una cuenta']").click()
    print(f"Diálogo cerrado: Usar sin una cuenta")
    time.sleep(2)
except:
    pass

try:
    driver.find_element(AppiumBy.XPATH, "//*[@text='Sí, acepto']").click()
    print(f"Diálogo cerrado: Sí, acepto")
    time.sleep(2)
except:
    pass

try:
    driver.find_element(AppiumBy.XPATH, "//*[@text='Más']").click()
    print(f"Diálogo cerrado: Más")
    time.sleep(2)
except:
    pass

try:
    driver.find_element(AppiumBy.XPATH, "//*[@text='Entendido']").click()
    print(f"Diálogo cerrado: Entendido")
    time.sleep(2)
except:
    pass

time.sleep(3)  # Wait for the next screen to load
driver.get("https://automationexercise.com/")

wait = WebDriverWait(driver, 20)
try:
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text, 'Automation')]")))
    print("Página cargada correctamente.")
except:
    print("No se pudo verificar la carga de la página.")

print(driver.contexts)
driver.switch_to.context('WEBVIEW_chrome')
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-image-wrapper")))
productos = driver.find_elements(By.CLASS_NAME, "product-image-wrapper")
print(f"✅ Se encontraron {len(productos)} productos.")


