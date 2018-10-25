@Remover_dado
Feature: remover dados de contato

   Feature Description: removendo um dado de contato no perfil
	
	Background:
		Given acesso a pagina de contatos da aplicacao
		
	Scenario: remover email
		When clico no icone para excluir o email desejado
		When clico em ok para confirmar o alert
		Then uma toastmessage aparece com o texto Rest in peace, dear email!
		
	Scenario: adicionar telefone
		When clico no icone para excluir o telefone desejado
		When clico em ok para confirmar o alert
		Then uma toastmessage aparece com o texto Rest in peace, dear phone!
		