"""
 * Programa para calcular a quantidade de litros a serem abastecidos de acordo com valor do litro e valor total a pagar, após, exibir o resultado em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

tipo  = input("Informe o tipo de combustivel: ")
litros = float(input("Informe a quantidade de litros: "))


match tipo:
    case "A":
        if litros <= 20:
            valor_total = litros * 2.9 - (litros * 2.9 * 0.03)
        else:
            valor_total = litros * 2.9 - (litros * 2.9 * 0.05);
    case "G":
        if litros <= 20:
            valor_total = litros * 3.3 - (litros * 3.3 * 0.04);
        else:
            valor_total = litros * 3.3 - (litros * 3.3 * 0.06);
    case _:
        print(f"Tipo digitado não correspondente")

print(f"O valor total a ser pago pelo cliente é de R$ {valor_total}")


