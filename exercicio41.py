"""
 * Programa para ler 2 valores e verificar o maior para exibir em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

num1 = float(input("Informe um número: "));
num2 = float(input("Informe outro número: "));

#ternario

print(f"O maior valor é {num1}") if num1 > num2 else print(f"O maior valor é {num2}")