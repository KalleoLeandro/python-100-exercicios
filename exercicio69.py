"""
 * Programa para imprimir um intervalo fechado de números de 1 a n, com n informado pelo usuário
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

n = 0

while n >= 0:
    n = int(input("Informe um número: "))
    for i in range(1,n + 1, 1):
        print(f"{i}")
	