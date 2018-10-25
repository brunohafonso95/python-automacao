@Adicionar_dado
Feature: adicionar dados de contato

  Feature Description: adicionando um dado de contato no perfil
	
	Background:
		Given acesso a pagina de perfil da aplicacao
		
	Scenario: adicionar email
		When seleciono a opcao email no combobox do modal
		When preencho o email e clico em save
		Then uma toastmessage aparece com o texto Your contact has been added!
	
	Scenario: adicionar email sem preencher o campo email
		When seleciono a opcao email no combobox do modal
		When deixo o campo do dado em branco e clico em save
		Then uma toastmessage aparece com o texto I think that you forget to tell me something!
		
	Scenario: adicionar telefone
		When seleciono a opcao phone no combobox do modal
		When preencho o telefone e clico em save
		Then uma toastmessage aparece com o texto Your contact has been added!
		
	Scenario: adicionar telefone sem preencher o campo telefone
		When seleciono a opcao phone no combobox do modal
		When deixo o campo do dado em branco e clico em save
		Then uma toastmessage aparece com o texto I think that you forget to tell me something!
		