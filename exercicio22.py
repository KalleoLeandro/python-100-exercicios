"""
 * Programa para exibir o salário final do vendedor com os valores informado pelo usuário 
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

salario_base = float(input("Informe o valor do salario base do funcionário: "));
carros_vendidos = int(input("Informe o número de carros vendidos pelo funcionáriol: "));
valor_venda = float(input("Informe o valor das vendas do funcionário: "))
comissao = float(input("Informe o valor da comissão por carro vendido pelo funcionário: "))

salario_final = salario_base + (carros_vendidos * comissao) + (valor_venda * 0.05);

print(f"O salário final do vendedor é de R${salario_final}");


