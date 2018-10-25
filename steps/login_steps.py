from behave import *
    
@given(u'acesso a pagina principal da aplicacao')
def step_impl(context):
    pass
    
@when(u'clico em Sign in')
def step_impl(context):
    context.taskit_main_page.clicar_botao_login_menu()
      
@when(u'preencho minhas credenciais de acesso e clico e SIGN IN')
def step_impl(context):
    context.taskit_main_page.preencher_login()
    context.taskit_main_page.preencher_senha()
    context.taskit_main_page.clicar_botao_login_modal()
     
@then(u'a mensagem hi, nome do usuario aparece no menu')
def step_impl(context):
    context.taskit_main_page.verificar_login()

@when(u'preencho minhas credenciais de acesso (nome de usuario incorreto) e clico e SIGN IN')
def step_impl(context):
    context.taskit_main_page.preencher_login("abcdef")
    context.taskit_main_page.preencher_senha()
    context.taskit_main_page.clicar_botao_login_modal()


@then(u'uma toastmessage aparece com o texto Maybe you brain dropped the password or login in some place!')
def step_impl(context):
    context.taskit_perfil_page.validar_toast_mensagem("Maybe you brain dropped the password or login in some place!")


@when(u'preencho minhas credenciais de acesso (senha incorreta) e clico e SIGN IN')
def step_impl(context):
    context.taskit_main_page.preencher_login()
    context.taskit_main_page.preencher_senha("87654321")
    context.taskit_main_page.clicar_botao_login_modal()


@when(u'preencho minhas credenciais de acesso (nome do usuario em branco) e clico e SIGN IN')
def step_impl(context):
    context.taskit_main_page.preencher_login("")
    context.taskit_main_page.preencher_senha()
    context.taskit_main_page.clicar_botao_login_modal()


@when(u'preencho minhas credenciais de acesso (senha em branco) e clico e SIGN IN')
def step_impl(context):
    context.taskit_main_page.preencher_login()
    context.taskit_main_page.preencher_senha("")
    context.taskit_main_page.clicar_botao_login_modal()