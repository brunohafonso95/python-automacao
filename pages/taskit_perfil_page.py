from time import sleep
from selenium.webdriver.support.ui import Select
from Pyautomators.web_extensao import Alerta as alert
from pages.taskit_main_page import taskit_main_page

class taskit_perfil_page():
    
    def __init__(self, driver):
        self.driver = driver
        self.alert = alert(driver.get_driver())
        self.taskit_main_page = taskit_main_page(driver) 
        
    def clicar_botao_perfil(self):
        self.driver.clica("me", "class", 20)
        
    def clicar_secao_perfil(self, secao):
        self.driver.clica(secao, "link")
    
    def clicar_botao_adicionar(self):
        self.driver.clica("//*[@id='moredata']/div[2]/button", "xpath")
        
    def selecionar_tipo_contato(self, tipo_contato):
        element = self.driver.elemento("type", "name")
        select = Select(element)
        select.select_by_value(tipo_contato)
    
    def preencher_contato(self, contato):
        self.driver.escreve("contact", contato, "name", 10, 0.2)
    
    def clicar_botao_salvar_contato(self):
        self.driver.clica("SAVE", "link")
        
    def validar_toast_mensagem(self, mensagem):
        sleep(1)
        assert mensagem in self.driver.pegar_texto("#toast-container .toast", "css")
    
    def clicar_botao_remover_contato(self, dado):
        seletor_elemento = "//span[@class='title'][text()='" + dado + "']/following-sibling::a"
        self.driver.clica(seletor_elemento, "xpath")
    
    def aceitar_alert(self):
        self.alert.aceitar()
    
    def remover_dado_contato(self, dado):
        pass
    
    def acessar_secao_password(self):
        self.clicar_botao_perfil() 
        self.clicar_secao_perfil("SECRET, SHHHH!")
    
    def acessar_secao_contato(self):
        self.clicar_botao_perfil() 
        self.clicar_secao_perfil("MORE DATA ABOUT YOU")
    
    def preencher_password(self, senha="12345678"):
        self.driver.escreve("password", senha, "name")
    
    def clicar_botao_salvar_password(self):
        self.driver.clica("changeMyPassword", "id")
    
#     def adicionar_email(self):
#         self.driver.pagina("http://www.juliodelima.com.br/taskit/")
#         self.driver.maximiza()
#         self.taskit_main_page.login()
#         self.acessar_secao_contato()
#         self.clicar_botao_adicionar()
#         self.selecionar_tipo_contato("email")
#         self.preencher_contato("testando@testando.com")
#         self.clicar_botao_salvar_contato()
#         self.driver.fechar_programa()
#         
#     def adicionar_telefone(self):
#         self.driver.pagina("http://www.juliodelima.com.br/taskit/")
#         self.driver.maximiza()
#         self.taskit_main_page.login()
#         self.acessar_secao_contato()
#         self.clicar_botao_adicionar()
#         self.selecionar_tipo_contato("phone")
#         self.preencher_contato("(11) 12345-6789")
#         self.clicar_botao_salvar_contato()
#         self.driver.fechar_programa()