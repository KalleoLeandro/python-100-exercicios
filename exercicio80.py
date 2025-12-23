"""
 * Programa para imprimir o valor total em estoque e a média das mercadorias com base nos valores fornecidos pelo usuário
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

qt = 0
preco = 0

qt = int(input(f"Informe o número de produtos do estoque: "))
preco = float(input(f"Informe o preço unitário do produto: "))

print("O valor total em estoque é de R$ {:.2f}".format(preco * qt))
print("A média de preço das mercadorias é de R${:.2f}".format(qt / preco))