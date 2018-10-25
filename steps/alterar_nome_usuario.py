from behave import *

@given(u'acesso a pagina para alterar o nome de usuario')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given acesso a pagina para alterar o nome de usuario')


@when(u'preencho o campo nome do usuario e clico em change my name')
def step_impl(context):
    raise NotImplementedError(u'STEP: When preencho o campo nome do usuario e clico em change my name')


@then(u'uma toastmessage aparece com o texto Now you will be called nome_do_usuario!')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then uma toastmessage aparece com o texto Now you will be called nome_do_usuario!')


@when(u'deixo o campo nome do usuario em branco e clico em change my name')
def step_impl(context):
    raise NotImplementedError(u'STEP: When deixo o campo nome do usuario em branco e clico em change my name')


@then(u'uma toastmessage aparece com o texto Ask to change your name and do not tell it, does not make sense!')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then uma toastmessage aparece com o texto Ask to change your name and do not tell it, does not make sense!')
