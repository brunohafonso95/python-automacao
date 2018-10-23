from time import sleep

class taskit_main_page():
    
    def __init__(self, driver):
        self.driver = driver
    
    def clicar_botao_login_menu(self):
        self.driver.clica("Sign in", "link")
        
        
    def clicar_botao_login_modal(self):
        self.driver.clica("SIGN IN", "link")
        
        
    def preencher_login(self, login="brunohafonso"):
        self.driver.escreve("//*[@id='signinbox']/div[1]/form/div[2]/div[1]/input", login, "xpath")
        
    
    def preencher_senha(self, senha="12345678"):
        self.driver.escreve("//*[@id='signinbox']/div[1]/form/div[2]/div[2]/input", senha, "xpath")
        
    
    def verificar_login(self):
        assert "Hi, Bruno Afonso" in self.driver.pegar_texto("me", "class", 2)
    
    def login(self):
        self.clicar_botao_login_menu()
        self.preencher_login()
        self.preencher_senha()
        self.clicar_botao_login_modal()
        
        
        
        