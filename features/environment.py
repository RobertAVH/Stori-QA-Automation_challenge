from behave import *
from global_functions.Functions import Functions as gf
from Config.hooks import get_browser

nav = get_browser()

def before_feature(self,scenario):
    gf.create_appium_driver(self,navegador=get_browser())