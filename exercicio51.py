"""
 * Programa para ler 3 valores e multiplicar os 2 menores, após, exibir o resultado em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

if num1 > num2 and num1 > num3:
    produto = num2 * num3
elif num2 > num1 and num2 > num3:
    produto = num1 * num3
else:
    produto = num1 * num2

print(f"O produto dos dois menores valores é {produto}")

