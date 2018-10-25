"""		Pyautomator Framework de teste

			primeiro_projeto_python"""

from Pyautomators.web import Web
from time import sleep
from pages.taskit_main_page import taskit_main_page
from pages.taskit_perfil_page import taskit_perfil_page

def before_all(context):
	pass
	
def before_feature(context,feature):
	pass

def before_scenario(context,scenario):
	context.driver = Web('Chrome', './driver/chromedriver.exe')
	context.taskit_main_page = taskit_main_page(context.driver)
	context.taskit_perfil_page = taskit_perfil_page(context.driver)
	context.driver.pagina("http://www.juliodelima.com.br/taskit/")
	context.driver.maximiza()

def before_step(context,step):
	pass

def after_step(context,step):
	pass

def after_scenario(context,scenario):
	context.driver.fechar_programa()

def after_feature(context,feature):
	pass

def after_all(context):
    pass