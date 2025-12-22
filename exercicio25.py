"""
 * Programa para exibir a capacidade final obtida com base em valores informados pelo usuário
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

preco = float(input("Informe o preço do litro de combustível: "));
reais = float(input("Informe o valor a ser pago: "));


litros = reais / preco;

print(f"O total de litros abastecido é de {litros}");


