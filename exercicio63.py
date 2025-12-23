"""
 * Programa para validar a possiblidade de aposentadoria com base nos valores fornecidos pelo usuário, e exibido o resultado em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

codigo = int(input("Informe o codigo do funcionário"))
ano_nascimento = int(input("Informe o ano de nascimento do funcionário"))
ano_ingresso = int(input("Informe o ano de ingresso na empresa"))
		
	
tempo_trabalho = 2021 - ano_ingresso;				
idade = 2021 - ano_nascimento;		
		

if (idade >= 65 or tempo_trabalho >= 30) or (idade >= 60 and tempo_trabalho >= 25):
	print(f"Funcionário código: {codigo}\nRequerer aposentadoria")
else:
    print(f"Funcionário código: {codigo}\nNão requerer")
	
											  
	