import json
from typing import Dict, Any

import openpyxl
import pytest
from appium.options.common import AppiumOptions
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver import ChromeOptions as OpcionesChrome
from Config.Config import Config
from Config.Config_execution import *


class Functions(Config):
    ##########################################################################
    ##############   -=_Config DRIVERS_=-   #############################
    ##########################################################################
    def create_appium_driver(self, URL=Config.URL, navegador=Config.browser):
        print("\nDirectorio Base: " + Config.basedir)
        self.ventanas = {}
        print("----------------")
        print(navegador)
        print("---------------")
        cap_chrome: Dict[str, Any] = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "browserName": "chrome",
            "unicodeKeyboard":True,
            "resetKeyboard":True,
            "noReset":True
        }
        cap_firefox: Dict[str, Any] = {
            "platformName": "windows",
            "automationName": "Gecko",
            "browserName": "Firefox",
            "marionette":True,
            "moz:firefoxOptions": {
                "androidPackage": "org.mozilla.firefox",
            }
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=AppiumOptions().load_capabilities(cap))


        # if navegador.lower() == "chrome":
        #     options = OpcionesChrome()
        #     options.add_argument('start-maximized')
        #     self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # elif navegador.lower() == "edge":
        #     self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        # elif navegador.lower() == "firefox":
        #     self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        # elif navegador.lower() == "opera":
        # #     print("Opera browser isn't support by Selenium 4 this test will be run whit Chrome")
        #     webdriver_service = service.Service(OperaDriverManager().install())
        #     webdriver_service.start()
        #
        #     options = webdriver.ChromeOptions()
        #     options.add_experimental_option('w3c', True)
        #
            # self.driver = webdriver.Remote(webdriver_service.service_url, options=options)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(URL)
        self.ventanas = {'Principal': self.driver.window_handles[0]}
        return self.driver


    def tearDown(self):
        print("Se cerrará  el DRIVER")
        self.driver.quit()

    ##########################################################################
    ##############       -=_JSON     HANDLE _=-              #################
    ##########################################################################

    def get_json_file(self, file):
        json_path = Config.Json + "/" + file + '.json'
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                print("get_json_file: " + json_path)
        except FileNotFoundError:
            self.json_strings = False
            pytest.skip(u"get_json_file: No se encontro el Archivo " + file)
            Functions.tearDown(self)

    def get_entity(self, entity):
        if self.json_strings is False:
            print("Define el DOM para esta prueba")
        else:
            try:
                self.json_ValueToFind = self.json_strings[entity]["ValueToFind"]
                self.json_GetFieldBy = self.json_strings[entity]["GetFieldBy"]
                return True

            except KeyError:
                pytest.skip(u"get_entity: No se encontro la key a la cual se hace referencia: " + entity)
                # self.driver.close()
                Functions.tearDown(self)
                return None

    def get_elements(self, entity, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element(By.ID, self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element(By.NAME, self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element(By.XPATH, self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)

                print("get_elements: " + self.json_ValueToFind)
                return elements

            except NoSuchElementException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except TimeoutException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

    def wait_element(self, locator, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)

                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

            except TimeoutException:
                print(u"Esperar_Elemento: No presente " + locator)
                Functions.tearDown(self)
            except NoSuchElementException:
                print(u"Esperar_Elemento: No presente " + locator)
                Functions.tearDown(self)

    def fill_excel_report(self, excel=Config.Excel):
        value_col = []
        wb = openpyxl.load_workbook(Config.Excel)
        hoja = wb.active
        filas = hoja.max_row
        columnas = hoja.max_column
        Test_Case_ID = "validate " + self.texto
        Developer = "Developer" + str(filas)
        Test_group = "landing Page"
        Test_case_name = "Validate " + self.texto
        Priority_Severity = "1/4"
        Pre_conditions = "Pre-conditions"
        Test_data = "N/A"
        Test_Steps = "Open Site\nClick in New window\nValidar text " + self.texto
        Expected_Result = "Text should be in site"
        Tester = "tester" + str(filas)
        Actual_result = "Text isnt in front of the site"
        Status = "Fail"
        Comments = "Test automation failed"
        Test_Evidence = "Or the output"
        value_col = [Test_Case_ID, Developer, Test_group, Test_case_name, Priority_Severity, Pre_conditions, Test_data,
                     Test_Steps, Expected_Result, Tester, Actual_result, Status, Comments, Test_Evidence]
        for col in range(columnas):
            hoja.cell(row=int(filas + 1), column=col + 1, value=value_col[col])

            print("------------------------------------")
            print("El libro de excel utilizado es de es: " + Config.Excel)
            print("Se escribio en la celda " + str(col) + " el valor: " + str(value_col[col]))
            print("------------------------------------")
        wb.save(Config.Excel)
