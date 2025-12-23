"""
 * Programa para ler 3 valores e somar os 2 maiores, após, exibir o resultado em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

if num1 <= num2 and num1 <= num3:
    soma = num2 + num3
elif num2 <= num1 and num2 <= num3:
    soma = num1 + num3
else:
    soma = num1 + num2

print(f"A soma dos dois maiores valores é {soma}")

