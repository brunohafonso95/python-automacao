@Alterar_senha
Feature: alterar senha do perfil

  Feature Description: alterando a senha do perfil
	
	Background:
		Given acesso a pagina de alteracao de senha
		
	Scenario: alterando senha (preenchendo a senha)
		When preencho o campo senha e clico em save my password
		Then uma toastmessage aparece com o texto You have a new secret, please do not share it!
		
	Scenario: alterando senha (deixando a senha em branco)
		When deixo o campo senha em branco e clico em save my password
		Then uma toastmessage aparece com o texto Do not be afraid, we will not share your secret!
	
	
		