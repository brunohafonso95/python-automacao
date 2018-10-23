from time import sleep
from selenium.webdriver.support.ui import Select

class taskit_perfil_page():
    
    def __init__(self, driver):
        self.driver = driver
        
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
    
    def remover_dado_contato(self, dado):
        seletor_elemento = "//span[@class='title'][text()=" + "'" + dado + "'" + "]/following-sibling::a"
    
    def acessar_secao_adicionar_contato(self):
        self.clicar_botao_perfil() 
        self.clicar_secao_perfil("MORE DATA ABOUT YOU")
        