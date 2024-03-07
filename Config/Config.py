import os
class Config():
	# Directorio Base
	basedir = os.path.abspath(os.path.join(__file__, '../..'))
	# JsonData
	Json = basedir + '/pages'
	Environment = 'Dev'
	# BROWSER DE PRUEBAS
	browser = 'chrome'
	# DIRECTORIO DE LA EVIDENCIA
	Path_Evidencias = basedir + '/data/capturas'
	# HOJA DE DATOS EXCEL
	Excel = basedir + '/data/RTM_for_QA_Tech_Challenge.xlsx'
	if Environment == 'Dev':
		URL = 'https://rahulshettyacademy.com/AutomationPractice/'