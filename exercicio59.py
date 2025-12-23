"""
  * Programa para calcular e exibir o resultado de uma compra, com base em uma comparação e exibir o resultado em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

macas = float(input("Informe o número de Kg de maças a serem adquiridas: "))
morangos = float(input("Informe o número de Kg de morangos a serem adquiridos: "))


if macas <= 5:
    total_macas = macas * 2.5
else:
    total_macas = macas * 2.2

if morangos <= 5:
    total_morangos = morangos * 1.8
else:
    total_morangos = morangos * 1.5

total = total_macas + total_morangos

if macas + morangos > 8 or total > 25:
    total = total - total * 0.1

print(f"O valor total a ser pago é de R${total}")


