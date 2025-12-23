"""
 * Programa para efetuar o cálculo de média aritmética com 2 notas, caso o valor seja fora do range de 0 a 10, solicitar novamente o valor
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

i = 1

while i < 0:
    nota = float(input("Informe uma nota: "))
    if nota >= 0 and nota <=10:
      media+=nota
      i += 1
    else:
       i = -1


print("A média do aluno é {:.1f}".format(media / 2))
	