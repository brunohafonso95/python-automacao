#@Alterar_nome_usuario
#Feature: alterar nome de usuario
#
#  Feature Description: alterando nome de usuario
#	
#	Background:
#		Given acesso a pagina para alterar o nome de usuario
#		
#	Scenario: inserir nome do usuario corretamente
#		When preencho o campo nome do usuario e clico em change my name
#		Then uma toastmessage aparece com o texto Now you will be called nome_do_usuario!
#	
#	Scenario: inserir nome do usuario (deixar campo em branco)
#		When deixo o campo nome do usuario em branco e clico em change my name
#		Then uma toastmessage aparece com o texto Ask to change your name and do not tell it, does not make sense!
#		