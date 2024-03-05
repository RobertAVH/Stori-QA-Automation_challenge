# -*- coding: utf-8 -*-
import time

import allure
import openpyxl
from behave import *
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from global_functions.Functions import Functions as gf

use_step_matcher("re")
global texto


class StepDefinitions():
    @step("I access to web site")
    def access_to_web_site(self):
        """
        step to access to the web site selected
        """
        with allure.step("Step 1"):
            gf.get_json_file(self, "challenge_page")
            #gf.create_appium_driver(self)
            # gf.wait_element(self, "logo", )


@step("I type (.*) in suggestion class input")
def type_in_suggestion_class(self, word):
    """
    :param word:
    """
    gf.get_json_file(self, "challenge_page")
    element = gf.get_elements(self, "ipt_suggestion_class")
    element.clear()
    element.send_keys(word)
    gf.wait_element(self, "options_suggestion")
    # self.driver.hide_keyboard()


@step("I select (.*) option")
def step_impl(self, country):
    """
    :type self: behave.runner.self
    """
    self.driver.find_element(By.XPATH, "//ul[@id='ui-id-1']/descendant::*[text()='" + country + "']").click()
    time.sleep(3)


@step("I select than (.*) the option (.*)")
def step_impl(self, obj, index):
    """
    :type context: behave.runner.Context
    """
    gf.get_json_file(self, "challenge_page")
    element = gf.get_elements(self, obj)
    select = Select(element)
    select.select_by_index(int(index))


@then("I wait to be able to see the change")
def step_impl(self):
    """
    :type context: behave.runner.Context
    """
    time.sleep(3)


@step("I do click in (.*)")
def step_impl(self, obj):
    """
    :type context: behave.runner.Context
    """
    gf.get_json_file(self, "challenge_page")
    element = gf.get_elements(self, obj)
    element.click()


@then("I switch the new window")
def step_impl(self):
    """
    :type context: behave.runner.Context
    """
    wait = WebDriverWait(self.driver, 20)
    original_window = self.ventanas["Principal"]
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in self.driver.window_handles:
        if window_handle != original_window:
            self.driver.switch_to.window(window_handle)
            break

    wait.until(EC.title_is("QAClick Academy - A Testing Academy to Learn, Earn and Shine"))


@step("I validate text (.*) in the page")
def step_impl(self, text):
    """
    :type context: behave.runner.Context
    """
    self.texto = text
    try:
        self.driver.find_element(By.XPATH, "//*[contains(text(),'" + str(text) + "')]")

    except NoSuchElementException:
        return text


@step("I report the bugs in excel report")
def step_impl(self):
    """
    :type context: behave.runner.Context
    """
    gf.fill_excel_report(self)


