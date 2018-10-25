from behave import *
from time import sleep
   
@given(u'acesso a pagina de contatos da aplicacao')
def step_impl(context):
    context.taskit_main_page.login()
    context.taskit_perfil_page.acessar_secao_contato()  
         
@when(u'clico no icone para excluir o email desejado')
def step_impl(context):
    context.taskit_perfil_page.clicar_botao_remover_contato("testando@testando.com.br")

@when(u'clico em ok para confirmar o alert')
def step_impl(context):
    context.taskit_perfil_page.aceitar_alert()
    
    
@then(u'uma toastmessage aparece com o texto Rest in peace, dear email!')
def step_impl(context):
    context.taskit_perfil_page.validar_toast_mensagem("Rest in peace, dear email!")
    
@when(u'clico no icone para excluir o telefone desejado')
def step_impl(context):
    context.taskit_perfil_page.clicar_botao_remover_contato("(11) 12345-6789")
   
    
@then(u'uma toastmessage aparece com o texto Rest in peace, dear phone!')
def step_impl(context):
    context.taskit_perfil_page.validar_toast_mensagem("Rest in peace, dear phone!")