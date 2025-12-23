"""
 * Programa para receber 10 valores e  calcular a média dos valores informados pelo usuário. Após, imprimir o resultado em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

valor = 0

for i in range(1,11,1):
    valor += float(input("Informe um número: "))    

valor / 10

print("A média aritmética dos valores é {:.2f}".format(valor))