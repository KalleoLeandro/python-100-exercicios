"""
 * Programa para verificar o menor valor entre os informados e exibir o mesmo em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

num1 = float(input("Informe o primeiro número"));
num2 = float(input("Informe o segundo número"));
num3 = float(input("Informe o terceiro número"));
		

		
if num1 < num2 and num1 < num3:
	print(f"O menor valor entre os valores digitados é " + num1)
elif(num2 < num1)and(num2 < num3):
	print(f"O menor valor entre os valores digitados é " + num2)
else:
	print(f"O menor valor entre os valores digitados é " + num3)
