from appium.webdriver.appium_service import AppiumService
from behave import *
from global_functions.Functions import Functions as gf


# global appium_service
# def before_all(self):
#     global appium_service
#     appium_service = AppiumService()
#     appium_service.start()


def before_feature(self, scenario):
    gf.create_appium_driver(self)

# def after_all(self):
#     global appium_service
#     appium_service.stop()