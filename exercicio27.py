"""
 * Programa para exibir o saldo total de venda com base em valores informados pelo usuário
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

p = int(input("Informe o número de camisetas P: "));
m = int(input("Informe o número de camisetas M: "));
g = int(input("Informe o número de camisetas G: "));


total = (p * 10) + (m * 12) + (g * 15);	

print(f"O Valor total da venda de camisetas é de R$ {total}");


