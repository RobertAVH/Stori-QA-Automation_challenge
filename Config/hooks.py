import subprocess
import sys


# class Hooks:
#
#
#     def __init__(self, browser):
#         self._browser = browser
#
#     def get_browser(self):
#         return self._browser
#
#     def set_browser(self, browser):
#         self._browser = browser
#
# _browser = get_text()
#
global browser
browser = ""

def get_browser():
    global browser
    return browser


def set_browser(value):
    global browser
    browser = value

browser = get_browser()

def config_execution(argv):
    global browser
    if type(argv) == str:
        browser = argv
    else:
        browser = argv[0].split("=")[1]
    # set_browser()
    p = subprocess.Popen(["powershell.exe",
                          "behave --junit -f behave_html_formatter:HTMLFormatter -o ./reports/report1.html -f pretty features"],
                         stdout=sys.stdout)
    p.communicate()
    print(p.communicate())
