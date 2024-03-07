# -*- coding: utf-8 -*-
import time

import allure
import openpyxl
from behave import *
from selenium.common import NoSuchElementException, MoveTargetOutOfBoundsException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from global_functions.Functions import Functions as gf

use_step_matcher("re")


class StepDefinitions():
    @step("I access to web site")
    def access_to_web_site(self):
        """
        step to access to the web site selected
        """
        gf.get_json_file(self, "challenge_page")
        # gf.create_appium_driver(self)
        gf.wait_element(self, "lbl_home_page", )


    @step("I type (.*) in suggestion class input")
    def type_text(self, word):
        """
        Step to type and validate the list wil be present
        :param word: word to type and validate against
        """
        gf.get_json_file(self, "challenge_page")
        element = gf.get_elements(self, "ipt_suggestion_class")
        element.clear()
        element.send_keys(word)
        gf.wait_element(self, "options_suggestion")


    @step("I select (.*) option")
    def select_option(self, country):
        """
        Step to select a option the select list
        :param country: country to select
        """
        self.driver.find_element(By.XPATH, "//ul[@id='ui-id-1']/descendant::*[text()='" + country + "']").click()
        time.sleep(3)


    @step("I select than (.*) the option (.*)")
    def select_than_option(self, obj, index):
        """
        Step to select a option the select list by index
        :param
            -obj: select object
            -index: index to select
        """
        gf.get_json_file(self, "challenge_page")
        element = gf.get_elements(self, obj)

        select = Select(element)
        select.select_by_index(int(index))


    @step("I wait to be able to see the change")
    def wait_tobe_able_to_see_the_change(self):
        """
        Wait some seconds by the change will be detected
        """
        time.sleep(3)


    @step("I do click in (.*)")
    def do_click_in_obj(self, obj):
        """
        step to do click in an object
        :param obj: object to click
        """
        gf.get_json_file(self, "challenge_page")
        element = gf.get_elements(self, obj)
        element.click()


    @step("I switch the new (.*)")
    def switch_the_new_window(self, type):
        """
        Step to switch the context in execution time
        :param
            -type:the switch to aply
        """
        wait = WebDriverWait(self.driver, 20)
        if type == "window":
            original_window = self.ventanas["Principal"]
            wait.until(EC.number_of_windows_to_be(2))
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break

            wait.until(EC.title_is("QAClick Academy - A Testing Academy to Learn, Earn and Shine"))
        elif type == "tab":
            gf.wait_element(self, "btn_menu")
            self.driver.switch_to.window(self.driver.window_handles[1])
        elif type == "alert":
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.alert_is_present())
            alert = Alert(self.driver)
            print(alert.text)  # Get the text of the alert
            alert.accept()
        elif type == "iframe":
            self.driver.switch_to.frame("courses-iframe")
        else:
            raise Exception("Option isn't enable")


    @step("I validate text (.*) in the page")
    def validate_text_in_page(self, text):
        """
        Step to validate some text exists in the front
        :param
            -text: Text to validate
        """
        self.texto = text
        try:
            self.driver.find_element(By.XPATH, "//*[contains(text(),'" + str(text) + "')]")

        except Exception:
            return text


    @step("I report the bugs in excel report")
    def report_the_bug_in_excel_report(self):
        """
        Step to update the excel file
        """
        gf.fill_excel_report(self)


    @step("I scroll to element (.*)")
    def scroll_to_element_feaature(self, obj):
        """
        Step to scroll to element
        :param
            -obj: Element to do scrolling
        """
        gf.scroll_to_element(self, obj)


    @step("I scroll page finding (.*) and take screenshot")
    def scroll_and_finding(self, object):
        """
        Step to scroll and take screenshot to find some element
        :param
            -object: name the object to find
        """
        pixels = 0
        window_size = self.driver.get_window_size()
        height = self.driver.execute_script("return document.body.scrollHeight")
        count_scrolls = height / window_size["height"]
        for x in range(int(count_scrolls)):
            time.sleep(0.5)
            try:
                # element = gf.get_elements(self, object)
                element = self.driver.find_element_by_xpath(By.XPATH, "//button[contains(text(),'VIEW ALL COURSES')]")
                gf.take_screenshot(self, self.scenario.name)
                break
            except:
                self.driver.execute_script("window.scrollTo(0, " + str(pixels) + ")")
                pixels = pixels + window_size['height']


    @step("I type (.*) in (.*) input")
    def type_in_input_element(self, text, obj):
        """
        Step to type in some input
        :param
            -text: text to type
            -obj: object to use
        """
        gf.get_json_file(self, "challenge_page")
        element = gf.get_elements(self, obj)
        element.clear()
        element.send_keys(text)


    @step("I get all the courses that cost \$(.*) and print its")
    def get_all_courses(self, cost):
        """
        Step for getting all the courses that especific cost and print some names
        :param
            -cost: cost to find in the table
        """
        names_courses = []
        table = gf.get_elements(self, "table_example")
        rows = table.find_elements(By.TAG_NAME, "tr")

        for row in range(2, len(rows)):
            cells = self.driver.find_element(By.XPATH,
                                             "//table[@id='product' and @name='courses']/tbody/tr[" + str(row) + "]/td[3]")
            names = self.driver.find_element(By.XPATH,
                                             "//table[@id='product' and @name='courses']/tbody/tr[" + str(row) + "]/td[2]")
            if cells.text == cost:
                names_courses.append(names.text.strip())

        print("There are", len(names_courses), "courses with cost $", cost, "\n it's names are:")
        for name in names_courses:
            print("\t-", name)


    @step("I get all the (.*) from fixed table")
    def get_the_profesion(self, profesion):
        """
        Step for getting all the people with the given profesion
        :param
            -profesion: profesion to find
        """
        names_courses = []
        table = gf.get_elements(self, "table_fixed")
        rows = table.find_elements(By.TAG_NAME, "tr")

        for row in range(2, len(rows)):
            cells = self.driver.find_element(By.XPATH,
                                             "//div[@class='tableFixHead']/table/tbody/tr[" + str(row) + "]/td[2]")
            names = self.driver.find_element(By.XPATH,
                                             "//div[@class='tableFixHead']/table/tbody/tr[" + str(row) + "]/td[1]")
            if cells.text == profesion:
                names_courses.append(names.text.strip())

        print("There are", len(names_courses), profesion, "\n he's names are:")
        for name in names_courses:
            print("\t-", name)


    @step("I get text and print the content the (.*) element")
    def get_text_and_print(self, obj):
        """
        Step to get the text and print from an element
        :param
            -obj: name to object by extracted text
        """
        element = gf.get_elements(self, obj)
        print(element.text)
