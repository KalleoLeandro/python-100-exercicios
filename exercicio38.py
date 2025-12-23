"""
 * Programa para calcular o custo de compra e exibir o resultado em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

macas = float(input("Informe a quantidade de maças a serem compradas: "));
	
if macas < 12:
    total = macas * 1.3;
else:
    total = macas;

print(f"O valor total da compra é de R$ {total}")