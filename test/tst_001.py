import time

import allure

from global_functions.Functions import Functions as Selenium
import unittest

@allure.feature
class test_001(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.create_driver(self)
        Selenium.get_json_file(self,"challenge_page")

    def test_001(self):
        Selenium.get_elements(self,"Logo")
        time.sleep(3)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()