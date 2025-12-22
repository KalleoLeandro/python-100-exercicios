"""
 * Programa para exibir o custo final para o consumidor com o valor de fábrica informado pelo usuário  
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

custo_inicial = float(input("Informe o valor de fábrica do automóvel: "));

custo_final = custo_inicial + (custo_inicial * 0.28) + (custo_inicial * 0.45);	

print(f"O custo final do veículo ao consumidor final é de R${custo_final}");


