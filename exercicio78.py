"""
 * Programa para ler 2 valores e efetuar a soma do intervalo fechado entre os valores. Após, imprimir em tela o resultado 
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

n1 = 0
n2 = 0
soma = 0

n1 = int(input(f"Informe um valor: "))

while n2 <= n1:
    n2 = int(input(f"Informe um valor: "))

for i in range(n1, n2, 1):
    soma += i

print(f"A soma do intervalo fechado é de {soma}")