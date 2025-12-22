"""
 * Programa para exibir o reajuste salarial com os valores  recebido do usuário
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

salario = float(input("Informe o salario: "));
reajuste = int(input("Informe o percentual de reajuste: "));

salario = salario + (salario * reajuste/100);


print(f"O salario reajustado do funcionário é de R${salario}");


