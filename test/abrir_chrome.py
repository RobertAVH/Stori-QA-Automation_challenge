import time
from typing import Dict, Any
from appium import webdriver
from appium.options.common import AppiumOptions

cap: Dict[str, Any] = {
  "platformName": "Android",
  # "appium:deviceName": "emu64xa",
  "appium:automationName": "UiAutomator2",
  # "appium:platformVersion": "14",
  "browserName": "chrome",
  # "appium:uuid": "emulator-5554"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=AppiumOptions().load_capabilities(cap))

driver.get("http:google.com")

time.sleep(3)

driver.close()
