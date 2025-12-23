"""
 * Programa par ler uma quantidade e depois uma quantidade de números baseado na primeira leitura. Após, imprimir o maior número e a média dos números lidos
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

num = 0
valor = 0
maior = 0
soma = 0

num = int(input(f"Informe uma quantidade: "))

valor = int(input(f"Informe um número: "))

maior = valor


for i in range(1,10,1):
    valor = int(input(f"Informe um número: "))
    soma += valor    
    if valor > maior:
        maior = valor

print("O maior valor é{:.2f}.\nA média aritmética dos números lidos é{:.2f}".format(maior, soma / num))