"""
 * Programa para ler o código e o preço de 5 produtos, após, imprimir a média aritmética e o maior preço lido em tela 
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

preco = 0
maior = 0
soma = 0

for i in range(0,5,1):
    codigo = input(f"Informe o código: ")
    preco = int(input(f"Informe o preço: "))
    soma += preco    
    if preco > maior:
        maior = preco

print("A média aritmética dos preços é{:.2f}.\nO maior preço informado é R${:.2f}".format(soma / 5, maior))