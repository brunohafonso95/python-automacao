from behave import *
   
@given(u'acesso a pagina de perfil da aplicacao')
def step_impl(context):
    context.taskit_main_page.login()
    context.taskit_perfil_page.acessar_secao_contato()
    context.taskit_perfil_page.clicar_botao_adicionar()
    
@when(u'seleciono a opcao email no combobox do modal')
def step_impl(context):
    context.taskit_perfil_page.selecionar_tipo_contato("email")
    
    
@when(u'preencho o email e clico em save')
def step_impl(context):
    context.taskit_perfil_page.preencher_contato("teste@teste.com")
    context.taskit_perfil_page.clicar_botao_salvar_contato()
    
@then(u'uma toastmessage aparece com o texto Your contact has been added!')
def step_impl(context):
    context.taskit_perfil_page.validar_toast_mensagem("Your contact has been added!")
    
    
@when(u'seleciono a opcao phone no combobox do modal')
def step_impl(context):
    context.taskit_perfil_page.selecionar_tipo_contato("phone")
    
@when(u'preencho o telefone e clico em save')
def step_impl(context):
    context.taskit_perfil_page.preencher_contato("(11) 12345-1234")
    context.taskit_perfil_page.clicar_botao_salvar_contato()
    
@when(u'deixo o campo do dado em branco e clico em save')
def step_impl(context):
    context.taskit_perfil_page.preencher_contato("")
    context.taskit_perfil_page.clicar_botao_salvar_contato()

@then(u'uma toastmessage aparece com o texto I think that you forget to tell me something!')
def step_impl(context):
    context.taskit_perfil_page.validar_toast_mensagem("I think that you forget to tell me something!")
