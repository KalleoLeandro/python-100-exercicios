"""
 * Programa para calcular o valor do salário de um vendedor e exibir o resultado em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

salario_base = float(input("Informe o salário base deste funcionário: "));
valor_vendas = float(input("Informe o valor total das vendas do mesmo funcionário: "));

	
if valor_vendas <=1500:
	total = salario_base + valor_vendas * 0.03;
else:
	total = salario_base + 1500 * 0.03 + (valor_vendas - 1500) * 0.05;

print(f"O salário final deste funcionário é de R${total}")