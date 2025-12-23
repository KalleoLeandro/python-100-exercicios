"""
 * Programa para calcular o salário de um funcionário e exibir o resultado em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

horas = float(input("Informe o total de horas trabalhadas: "));
valor_hora = float(input("Informe o valor das horas: "));

if horas <= 160:
	total = 160 * valor_hora;
else:
	total = 160 * valor_hora;
	total = total + ((horas - 160) * (valor_hora * 1.5));

print(f"O salário final deste funcionário é de R${total}")