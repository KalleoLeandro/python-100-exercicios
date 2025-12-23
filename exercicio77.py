"""
 * Programa para ler 10 númerose e efetuar a soma dos valores menores que 40. Após, imprimir os valores em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

n = 0
soma = 0

for i in range(1, 11,1):
    n = float(input(f"Informe um número: "))
    if n < 40:
        soma += n

print("A soma dos valores menores que 40 é de {:.2f}".format(soma))