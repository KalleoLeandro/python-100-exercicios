"""
 * Programa para ordenar valores em ordem crescente, e exibir em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

num1 = float(input("Informe um número: "));
num2 = float(input("Informe outro número: "));

#ternario

print(f"Os valores em ordem crescente são {num2} e {num1}") if num1 > num2 else print(f"Os valores em ordem crescente são {num1} e {num2}")