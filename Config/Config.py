import os
from .hooks import *

class Config():
    # Directorio Base
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    # JsonData
    Json = basedir + "/pages"

    Environment = 'Dev'

    # BROWSER DE PRUEBAS
    browser = "FIREFOX"

    # DIRECTORIO DE LA EVIDENCIA
    Path_Evidencias = basedir + '/output'

    # HOJA DE DATOS EXCEL
    Excel = basedir + '/data/RTM_for_QA_Tech_Challenge.xlsx'

    if Environment == 'Dev':
        URL = 'https://rahulshettyacademy.com/AutomationPractice/'


