from behave import *
from time import sleep

@given(u'acesso a pagina de alteracao de senha')
def step_impl(context):
    context.taskit_main_page.login()
    context.taskit_perfil_page.acessar_secao_password()

@when(u'preencho o campo senha e clico em save my password')
def step_impl(context):
    context.taskit_perfil_page.preencher_password()
    context.taskit_perfil_page.clicar_botao_salvar_password()

@then(u'uma toastmessage aparece com o texto You have a new secret, please do not share it!')
def step_impl(context):
    context.taskit_perfil_page.validar_toast_mensagem("You have a new secret, please do not share it!")

@when(u'deixo o campo senha em branco e clico em save my password')
def step_impl(context):
    context.taskit_perfil_page.preencher_password("")
    context.taskit_perfil_page.clicar_botao_salvar_password()

@then(u'uma toastmessage aparece com o texto Do not be afraid, we will not share your secret!')
def step_impl(context):
    context.taskit_perfil_page.validar_toast_mensagem("Do not be afraid, we will not share your secret!")