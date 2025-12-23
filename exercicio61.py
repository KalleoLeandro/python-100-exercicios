"""
 * Programa para ler a descrição, quantidade adquirida e preço unitário de um produto. Após, calcular e exibir o valor total do produto, o desconto, e o valor a pagar com desconto
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

descricao = input("Informe o nome do produto");
qt = int(input("Informe a quantidade a ser adquirida de um produto"))
preco = float(input("Informe o preco unitário do produto"))


total = qt * preco

if qt <= 5:
    total = total - total * 0.2
elif qt > 5 and qt < 10:
    total = total - total * 0.3
else:
    total = total - total * 0.5

print(f"O valor total a ser pago pelo produto {descricao} é de R${total}")