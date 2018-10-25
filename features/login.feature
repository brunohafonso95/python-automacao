@Login
Feature: login

  Feature Description: fazendo login na aplicacao
	Background: 
		Given acesso a pagina principal da aplicacao
		When clico em Sign in
	
	Scenario: login com dados corretos
		When preencho minhas credenciais de acesso e clico e SIGN IN
		Then a mensagem hi, nome do usuario aparece no menu
		
	Scenario: login com nome de usuario incorreto
		When preencho minhas credenciais de acesso (nome de usuario incorreto) e clico e SIGN IN
		Then uma toastmessage aparece com o texto Maybe you brain dropped the password or login in some place!
		
	Scenario: login com senha incorreta
		When preencho minhas credenciais de acesso (senha incorreta) e clico e SIGN IN
		Then uma toastmessage aparece com o texto Maybe you brain dropped the password or login in some place! 
		
	Scenario: login com nome de usuario em branco
		When preencho minhas credenciais de acesso (nome do usuario em branco) e clico e SIGN IN
		Then uma toastmessage aparece com o texto Maybe you brain dropped the password or login in some place!
		
	Scenario: login com senha em branco
		When preencho minhas credenciais de acesso (senha em branco) e clico e SIGN IN
		Then uma toastmessage aparece com o texto Maybe you brain dropped the password or login in some place!