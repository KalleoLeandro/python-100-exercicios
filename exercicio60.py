"""
 * Programa para ler um código de usuário e uma senha, validar e exibir o resultado de acordo com uma comparação
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

codigo = float(input("Informe o código do usuário: "))


if codigo == "1234":
	codigo = input(f"Informe a senha")
	if codigo == "9999":
		print(f"Acesso permitido")
	else:
		print(f"Senha incorreta")
else:
    print(f"Usuário inválido")