"""
 * Programa para calcular a soma de 10 números informados pelo usuário. Após, imprimir o resultado em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

soma = 0

for i in range(1, 11,1):
    soma += float(input(f"Informe um número: "))

print("A soma dos valores é {:.2f}".format(soma))