from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "12"
options.device_name = "a31"
options.automation_name = "UiAutomator2"
options.app_package = "com.sec.android.app.popupcalculator"
options.app_activity = ".Calculator t526"

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)




driver.find_element(AppiumBy.ID, "com.sec.android.app.popupcalculator:id/calc_keypad_btn_07").click()
driver.find_element(AppiumBy.ID, "com.sec.android.app.popupcalculator:id/calc_keypad_btn_add").click()
driver.find_element(AppiumBy.ID, "com.sec.android.app.popupcalculator:id/calc_keypad_btn_08").click()

driver.find_element(AppiumBy.ID, "com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal").click()

result = driver.find_element(AppiumBy.ID, "com.sec.android.app.popupcalculator:id/calc_edt_formula").text
print(f"Resultado de la suma: {result}")
