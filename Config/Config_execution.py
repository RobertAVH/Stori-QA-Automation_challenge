import subprocess
import sys

def config_execution(argv):
    global browser

    if type(argv) == str:
        browser = argv
    else:
        browser = argv[0].split("=")[1]
    edit_browser(browser)
    p = subprocess.Popen(["powershell.exe",
                          "behave --junit -f behave_html_formatter:HTMLFormatter -o ./reports/report1.html -f pretty features"],
                         stdout=sys.stdout)
    p.communicate()
    print(p.communicate())


def edit_browser(browser):
    with open("./Config/Config.py", "w", encoding="utf-8") as file:
        filas = file.write(""\
"import os\n\
class Config():\n\
\t# Directorio Base\n\
\tbasedir = os.path.abspath(os.path.join(__file__, '../..'))\n\
\t# JsonData\n\
\tJson = basedir + '/pages'\n\
\tEnvironment = 'Dev'\n\
\t# BROWSER DE PRUEBAS\n\
\tbrowser = '" + browser + "'\n\
\t# DIRECTORIO DE LA EVIDENCIA\n\
\tPath_Evidencias = basedir + '/data/capturas'\n\
\t# HOJA DE DATOS EXCEL\n\
\tExcel = basedir + '/data/RTM_for_QA_Tech_Challenge.xlsx'\n\
\tif Environment == 'Dev':\n\
\t\tURL = 'https://rahulshettyacademy.com/AutomationPractice/'"
        )
        file.close()
