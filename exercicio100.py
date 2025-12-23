"""
 * Programa para ler e armazenar os valores das temperaturas dos 7 dias da semana em um array.
  Calcular a menor e a maior temperatura registrada,a média das temperaturas,
   e os dias em que a temperatura foi menor que a média. Imprimir esses valores em tela. 
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

temperaturas = []
maior = 0
menor = 0
media = 0
qt = 0
dia = ""

for i in range(7):
    match i:
        case 0:
            dia = "da segunda-feira"
        case 1:
            dia = "da terça-feira"
        case 2:
            dia = "da quarta-feira"
        case 3:
            dia = "da quinta-feira"
        case 4:
            dia = "da sexta-feira"
        case 5:
            dia = "do sábado"
        case 6:
            dia = "do domingo"

    temperaturas.append(float(input("Informe a temperatura " + dia)))

maior = temperaturas[0]
menor = temperaturas[0]

for i in range(7):
    media+=temperaturas[i]
    if temperaturas[i] > maior:
        maior = temperaturas[i]
    if temperaturas[i] < menor:
        menor = temperaturas[i]

media /= len(temperaturas)

for i in range(len(temperaturas)):
    if temperaturas[i] > media:
        qt += 1


if maior == menor:
    print(f"A temperatura se manteve constante ao longo da semana sendo de {maior}° C.\nA média de temperaturas foi de {media}° C.\nComo todos os dias tiveram a mesma temperatura, todos estão dentro da média semanal")
else:
    print(f"A maior temperatura registrada foi de {maior}° C.\nA menor temperatura foi de {menor}° C.\nA média foi de {media}° C.\nA quantidade de dias acima da média foi de {qt} dias")