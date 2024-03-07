from appium.webdriver.appium_service import AppiumService
from global_functions.Functions import Functions as gf


def before_all(self):
    gf.start_appium(self)


def before_scenario(self,scenario):
    gf.create_appium_driver(self)


def after_scenario(self,scenario):
    gf.tearDown(self)

def before_step(self, step):
    self.step = step

def after_all(self):
    gf.stop_appium(self)
