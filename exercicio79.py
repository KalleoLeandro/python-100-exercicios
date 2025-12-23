"""
 * Programa para calcular e imprimir o resultado da média aritmética do intervalo fechado de inteiros de 15 a 100
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

n1 = 0
soma = 0

for i in range(15, 101, 1):
    soma += i
    n += 1

print("A média aritmética do intervalo fechado de 15 a 100 é de {:.2f}".format(soma/n))